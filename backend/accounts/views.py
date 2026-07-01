"""
Endpoints d'authentification (Lot 3 : email-identifiant + validation + reset).

    POST /api/accounts/signup/                  — créer un compte (par email)
    POST /api/accounts/login/                   — se connecter (par email) -> token
    POST /api/accounts/logout/                  — se déconnecter
    GET  /api/accounts/me/                       — utilisateur courant (+ email_verified)
    POST /api/accounts/verify-email/             — confirmer l'email (token du lien)
    POST /api/accounts/resend-verification/      — renvoyer l'email de validation
    POST /api/accounts/password-reset/           — demander un reset (envoie un email)
    POST /api/accounts/password-reset/confirm/   — définir le nouveau mot de passe
"""

import csv
import hashlib
import io
import json
import logging

from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.utils import timezone as django_timezone
from drf_spectacular.utils import OpenApiResponse, extend_schema
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .emails import EmailError, send_password_reset_email, send_verification_email
from .models import DataRequest, get_or_create_profile
from .serializers import (
    ChangePasswordSerializer,
    DeleteAccountSerializer,
    EmailVerifySerializer,
    LoginSerializer,
    PasswordResetConfirmSerializer,
    PasswordResetRequestSerializer,
    ProfileUpdateSerializer,
    SignupSerializer,
    UserSerializer,
)
from .tokens import read_email_verify_token, read_password_reset_tokens

logger = logging.getLogger(__name__)


class SignupView(APIView):
    """Inscription par email. Envoie l'email de validation (best-effort)."""

    permission_classes = [AllowAny]
    authentication_classes = []  # endpoint public : pas de CSRF via session (cf. LoginView)

    @extend_schema(request=SignupSerializer, responses={201: UserSerializer})
    def post(self, request):
        # Lot 8 : l'admin peut fermer les inscriptions depuis l'interface.
        from administration.models import SiteConfig

        if not SiteConfig.load().allow_signups:
            return Response(
                {"detail": "Les inscriptions sont actuellement fermées."},
                status=status.HTTP_403_FORBIDDEN,
            )

        serializer = SignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Validation SOFT : on tente d'envoyer l'email de confirmation, mais on
        # NE bloque PAS l'inscription si l'envoi échoue (clé Brevo expirée, etc.).
        try:
            send_verification_email(user)
        except EmailError as exc:
            logger.warning("Email de validation non envoyé pour %s : %s", user.email, exc)

        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    """Connexion par email + mot de passe. Renvoie un token DRF + crée la session."""

    permission_classes = [AllowAny]
    # Endpoint PUBLIC (pré-auth) : on désactive l'authentification de requête.
    # Sinon DRF SessionAuthentication, dès qu'un cookie `sessionid` résiduel est
    # présent (posé par django_login au login précédent), impose un contrôle CSRF
    # et rejette l'appel : « CSRF Failed: CSRF token missing ». Le frontend
    # s'authentifie par token, pas par session — il n'envoie pas de jeton CSRF.
    authentication_classes = []

    @extend_schema(
        request=LoginSerializer, responses={200: OpenApiResponse(description="{ token, user }")}
    )
    def post(self, request):
        serializer = LoginSerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]

        token, _ = Token.objects.get_or_create(user=user)
        django_login(request, user)  # session utile pour la Swagger UI
        return Response({"token": token.key, "user": UserSerializer(user).data})


class LogoutView(APIView):
    """Déconnexion : invalide le token + détruit la session."""

    permission_classes = [IsAuthenticated]

    @extend_schema(responses={204: OpenApiResponse(description="Déconnexion réussie")})
    def post(self, request):
        Token.objects.filter(user=request.user).delete()
        django_logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)


class MeView(APIView):
    """Renvoie l'utilisateur connecté (avec email_verified pour le bandeau front)."""

    permission_classes = [IsAuthenticated]

    @extend_schema(responses={200: UserSerializer})
    def get(self, request):
        return Response(UserSerializer(request.user).data)


class VerifyEmailView(APIView):
    """Confirme l'adresse email à partir du token reçu par email."""

    permission_classes = [AllowAny]
    authentication_classes = []  # endpoint public : pas de CSRF via session (cf. LoginView)

    @extend_schema(
        request=EmailVerifySerializer,
        responses={200: OpenApiResponse(description="Email confirmé")},
    )
    def post(self, request):
        serializer = EmailVerifySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        uid = read_email_verify_token(serializer.validated_data["token"])
        if uid is None:
            return Response(
                {"detail": "Lien de validation invalide ou expiré."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            user = User.objects.get(pk=uid)
        except User.DoesNotExist:
            return Response(
                {"detail": "Utilisateur introuvable."}, status=status.HTTP_400_BAD_REQUEST
            )

        profile = get_or_create_profile(user)
        profile.email_verified = True
        profile.save(update_fields=["email_verified"])
        return Response({"detail": "Adresse email confirmée avec succès."})


class ResendVerificationView(APIView):
    """Renvoie l'email de validation à l'utilisateur connecté."""

    permission_classes = [IsAuthenticated]

    @extend_schema(responses={200: OpenApiResponse(description="Email renvoyé")})
    def post(self, request):
        if get_or_create_profile(request.user).email_verified:
            return Response({"detail": "Votre email est déjà confirmé."})
        try:
            send_verification_email(request.user)
        except EmailError as exc:
            return Response({"detail": str(exc)}, status=status.HTTP_502_BAD_GATEWAY)
        return Response({"detail": "Email de validation renvoyé."})


class PasswordResetRequestView(APIView):
    """Demande de réinitialisation : envoie un email avec un lien (si le compte existe)."""

    permission_classes = [AllowAny]
    authentication_classes = []  # endpoint public : pas de CSRF via session (cf. LoginView)

    @extend_schema(
        request=PasswordResetRequestSerializer,
        responses={200: OpenApiResponse(description="Email envoyé si le compte existe")},
    )
    def post(self, request):
        serializer = PasswordResetRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data["email"].strip().lower()

        user = User.objects.filter(email__iexact=email).first()
        if user is not None:
            try:
                send_password_reset_email(user)
            except EmailError as exc:
                logger.warning("Email de reset non envoyé pour %s : %s", email, exc)

        # Anti-énumération : réponse IDENTIQUE que le compte existe ou non
        # (on ne révèle pas quels emails sont enregistrés).
        return Response(
            {
                "detail": "Si un compte existe pour cet email, un lien "
                "de réinitialisation vient d'être envoyé."
            }
        )


class PasswordResetConfirmView(APIView):
    """Définit le nouveau mot de passe à partir du lien (uid + token)."""

    permission_classes = [AllowAny]
    authentication_classes = []  # endpoint public : pas de CSRF via session (cf. LoginView)

    @extend_schema(
        request=PasswordResetConfirmSerializer,
        responses={200: OpenApiResponse(description="Mot de passe réinitialisé")},
    )
    def post(self, request):
        serializer = PasswordResetConfirmSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = read_password_reset_tokens(
            serializer.validated_data["uid"], serializer.validated_data["token"]
        )
        if user is None:
            return Response(
                {"detail": "Lien de réinitialisation invalide ou expiré."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user.set_password(serializer.validated_data["new_password"])
        user.save(update_fields=["password"])
        return Response({"detail": "Mot de passe réinitialisé. Vous pouvez vous connecter."})


# ---------------------------------------------------------------------------
# Gestion du profil (Lot 4)
# ---------------------------------------------------------------------------


class ProfileView(APIView):
    """Profil de l'utilisateur connecté : consulter, modifier, supprimer.

    GET    /api/accounts/profile/  — lire son profil
    PATCH  /api/accounts/profile/  — modifier prénom / nom / email
    DELETE /api/accounts/profile/  — supprimer définitivement son compte
    """

    permission_classes = [IsAuthenticated]

    @extend_schema(responses={200: UserSerializer})
    def get(self, request):
        return Response(UserSerializer(request.user).data)

    @extend_schema(request=ProfileUpdateSerializer, responses={200: UserSerializer})
    def patch(self, request):
        serializer = ProfileUpdateSerializer(instance=request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Si l'email a changé, on (re)envoie un email de validation (best-effort,
        # validation SOFT : on ne bloque pas si l'envoi échoue).
        if getattr(user, "_email_changed", False):
            try:
                send_verification_email(user)
            except EmailError as exc:
                logger.warning("Email de validation non renvoyé pour %s : %s", user.email, exc)

        return Response(UserSerializer(user).data)

    @extend_schema(
        request=DeleteAccountSerializer,
        responses={204: OpenApiResponse(description="Compte supprimé")},
    )
    def delete(self, request):
        # Suppression DURE (hard delete) : confirmée par le mot de passe.
        serializer = DeleteAccountSerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)

        user = request.user
        Token.objects.filter(user=user).delete()  # invalide le token courant
        django_logout(request)
        user.delete()  # supprime aussi le Profile (on_delete=CASCADE)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ExportDataView(APIView):
    """Export RGPD Art. 15 — toutes les données personnelles de l'utilisateur.

    GET /api/accounts/me/export/?format=json   (défaut)
    GET /api/accounts/me/export/?format=csv
    """

    permission_classes = [IsAuthenticated]

    @extend_schema(responses={200: OpenApiResponse(description="Fichier d'export (JSON ou CSV)")})
    def get(self, request):
        fmt = request.query_params.get("format", "json").lower()
        if fmt not in ("json", "csv"):
            return Response(
                {"detail": "Format invalide. Valeurs acceptées : json, csv."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = request.user
        profile = get_or_create_profile(user)

        # Collecte des données — filtrage STRICT par request.user (jamais d'autres users)
        quizzes_qs = user.quizzes.prefetch_related("questions").order_by("-created_at")
        sar_qs = user.data_requests.all()

        # Catégorie 2 : métadonnées des quiz (sans questions — séparées ci-dessous)
        quizzes_data = [
            {
                "id": q.id,
                "title": q.title,
                "created_at": q.created_at.isoformat(),
            }
            for q in quizzes_qs
        ]

        # Catégorie 3 : réponses données par l'utilisateur (une ligne par question)
        responses_data = [
            {
                "quiz_id": q.id,
                "quiz_title": q.title,
                "question_index": qu.index,
                "question_prompt": qu.prompt,
                "selected_index": qu.selected_index,
                "correct_index": qu.correct_index,
                "is_correct": qu.selected_index == qu.correct_index,
            }
            for q in quizzes_qs
            for qu in q.questions.all()
        ]

        # Catégorie 4 : historique des scores (Art. 15 — progression pédagogique)
        score_history_data = [
            {
                "quiz_id": q.id,
                "quiz_title": q.title,
                "score": q.score,
                "date": q.created_at.isoformat(),
            }
            for q in quizzes_qs
        ]

        # Catégorie 5 : journal des demandes SAR (audit trail)
        sar_logs_data = [
            {
                "requested_at": r.requested_at.isoformat(),
                "status": r.status,
                "responded_at": r.responded_at.isoformat() if r.responded_at else None,
                "file_hash": r.file_hash or None,
            }
            for r in sar_qs
        ]

        export_payload = {
            "exported_at": django_timezone.now().isoformat(),
            # Catégorie 1 : données du profil utilisateur
            "user_profile": {
                "email": user.email,
                "username": user.username,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "date_joined": user.date_joined.isoformat(),
                "email_verified": profile.email_verified,
            },
            # Catégorie 2 : quiz créés
            "quizzes": quizzes_data,
            # Catégorie 3 : réponses aux questions (Art. 15 — portabilité)
            "quiz_responses": responses_data,
            # Catégorie 4 : historique des scores (progression pédagogique)
            "score_history": score_history_data,
            # Catégorie 5 : journal SAR (audit trail Art. 15)
            "sar_logs": sar_logs_data,
            # Catégorie 6 : mentions légales et coordonnées RGPD
            "legal_notice": {
                "dpo_contact": "dpo@edututor.fr",
                "retention_years": 3,
                "policy_url": "/legal/privacy",
                "deletion_right": "Art. 17 RGPD — contacter dpo@edututor.fr",
                "portability_right": "Art. 20 RGPD — cet export constitue la réponse",
            },
        }

        timestamp = django_timezone.now().strftime("%Y%m%d_%H%M%S")
        safe_email = user.email.replace("@", "_at_").replace(".", "_")

        if fmt == "json":
            content = json.dumps(export_payload, ensure_ascii=False, indent=2)
            content_bytes = content.encode("utf-8")
            file_hash = hashlib.sha256(content_bytes).hexdigest()
            filename = f"edututor_export_{safe_email}_{timestamp}.json"
            response = HttpResponse(content_bytes, content_type="application/json; charset=utf-8")
        else:
            # CSV multi-section : une section par catégorie RGPD (6 au total)
            output = io.StringIO()
            writer = csv.writer(output)

            writer.writerow(["## CATEGORIE 1 : PROFIL UTILISATEUR"])
            writer.writerow(["email", "username", "first_name", "last_name", "date_joined", "email_verified"])
            p = export_payload["user_profile"]
            writer.writerow([p["email"], p["username"], p["first_name"], p["last_name"], p["date_joined"], p["email_verified"]])

            writer.writerow([])
            writer.writerow(["## CATEGORIE 2 : QUIZ"])
            writer.writerow(["quiz_id", "title", "created_at"])
            for q in export_payload["quizzes"]:
                writer.writerow([q["id"], q["title"], q["created_at"]])

            writer.writerow([])
            writer.writerow(["## CATEGORIE 3 : REPONSES AUX QUESTIONS"])
            writer.writerow(["quiz_id", "quiz_title", "question_index", "question_prompt", "selected_index", "correct_index", "is_correct"])
            for r in export_payload["quiz_responses"]:
                writer.writerow([r["quiz_id"], r["quiz_title"], r["question_index"], r["question_prompt"], r["selected_index"], r["correct_index"], r["is_correct"]])

            writer.writerow([])
            writer.writerow(["## CATEGORIE 4 : HISTORIQUE DES SCORES"])
            writer.writerow(["quiz_id", "quiz_title", "score", "date"])
            for s in export_payload["score_history"]:
                writer.writerow([s["quiz_id"], s["quiz_title"], s["score"], s["date"]])

            writer.writerow([])
            writer.writerow(["## CATEGORIE 5 : JOURNAL SAR (demandes RGPD)"])
            writer.writerow(["requested_at", "status", "responded_at", "file_hash"])
            for log in export_payload["sar_logs"]:
                writer.writerow([log["requested_at"], log["status"], log["responded_at"] or "", log["file_hash"] or ""])

            writer.writerow([])
            writer.writerow(["## CATEGORIE 6 : MENTIONS LEGALES"])
            writer.writerow(["dpo_contact", "retention_years", "policy_url", "deletion_right"])
            lg = export_payload["legal_notice"]
            writer.writerow([lg["dpo_contact"], lg["retention_years"], lg["policy_url"], lg["deletion_right"]])

            content = output.getvalue()
            content_bytes = content.encode("utf-8")
            file_hash = hashlib.sha256(content_bytes).hexdigest()
            filename = f"edututor_export_{safe_email}_{timestamp}.csv"
            response = HttpResponse(content_bytes, content_type="text/csv; charset=utf-8")

        # Audit trail SAR
        sar = DataRequest.objects.create(user=user, file_hash=file_hash)
        sar.status = DataRequest.STATUS_COMPLETED
        sar.responded_at = django_timezone.now()
        sar.save(update_fields=["status", "responded_at"])

        response["Content-Disposition"] = f'attachment; filename="{filename}"'
        return response


class ChangePasswordView(APIView):
    """Changement de mot de passe (en étant connecté, avec l'ancien mot de passe)."""

    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=ChangePasswordSerializer,
        responses={200: OpenApiResponse(description="Mot de passe modifié")},
    )
    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)

        user = request.user
        user.set_password(serializer.validated_data["new_password"])
        user.save(update_fields=["password"])

        # Changer le mot de passe invalide les tokens DRF existants : on en
        # régénère un pour que l'utilisateur reste connecté sans avoir à se
        # reconnecter manuellement.
        Token.objects.filter(user=user).delete()
        token = Token.objects.create(user=user)
        return Response({"detail": "Mot de passe modifié.", "token": token.key})
