# Product Backlog — EduTutor IA

**APOCAL'IPSSI** · CADRAGE MATINAL · ARTEFACT 2 SUR 7
Projet EduTutor IA · Édition 2026 · Semaine immersive Scrum


## Identification

| Champ            | Valeur                                                                                                                                     |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Equipe n°       | 16                                                                                                                                         |
| Membres          | Rania ZERAMDINI, Amani LAYOUNI, Badreddine CHEBBOUR, Taise de These NGANGA YABIE, Noah MASSET, Awadi BEDJA MROINKODO SAID, Clement BASTIEN |
| Sprint concerné | Cadrage                                                                                                                                    |
| Version          | v1.1 — intègre perturbation J1                                                                                                           |
| Date de remise   | 30/06/2026 09h00                                                                                                                           |
| Statut           | En revue PO                                                                                                                                |

---

## Contexte du projet

EduTutor IA est une plateforme brownfield : le code F1–F6 existe, tourne en local, mais n'est ni testé, ni stabilisé, ni conforme RGPD. Les bugs connus (PDF corrompu → 500 silencieux, timeout LLM 600 s, absence de rate limiting, prompt injection) constituent la dette technique prioritaire. Les stories MUST ne sont pas des fonctionnalités nouvelles — ce sont des engagements de qualité, de fiabilité et de couverture de tests sur des features existantes.

La perturbation J1 (lundi matin, cadrage) a introduit Mme Sophie Lefèvre comme cible secondaire. Ses stories ne sont pas MUST : la priorité R1 reste le parcours étudiant complet (F1–F6) livré à mercredi 17h45.

---

## Epics

| ID    | Epic                       | Activité utilisateur              | Stories             |
| ----- | -------------------------- | ---------------------------------- | ------------------- |
| EP-01 | Identification utilisateur | S'inscrire, se connecter           | US-01, US-07, US-13 |
| EP-02 | Gestion de contenu         | Uploader un cours                  | US-02, US-08, US-14 |
| EP-03 | Génération de quiz       | Générer un quiz                  | US-03, US-09, US-15 |
| EP-04 | Passage de quiz            | Passer le quiz et voir le score    | US-04, US-05, US-10 |
| EP-05 | Suivi de progression       | Consulter résultats et historique | US-06, US-11, US-16 |
| EP-06 | Conformité et admin       | Gérer son compte, RGPD            | US-12, US-17        |
| EP-07 | Espace enseignant (J1)     | Suivi de classe                    | US-21, US-22, US-23 |

---

## MUST — Release 1, à livrer mercredi 2 juillet 17h45

| ID    | User Story                                                                                                                                            | Persona     | SP | Sprint |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | -- | ------ |
| US-01 | En tant qu'étudiant·e, je veux créer un compte avec email et mot de passe, afin de sauvegarder mes quiz et y revenir quand je veux.                | Léa Martin | 3  | S1     |
| US-02 | En tant qu'étudiant·e, je veux uploader un PDF (≤ 5 Mo) ou saisir un texte de cours (≥ 200 car.), afin de ne pas recopier mon support à la main. | Léa Martin | 5  | S1     |
| US-03 | En tant qu'étudiant·e, je veux générer un quiz de 10 QCM en moins de 60 s à partir de mon cours, afin de réviser rapidement un chapitre.        | Léa Martin | 8  | S2     |
| US-04 | En tant qu'étudiant·e, je veux soumettre mes réponses et obtenir une correction automatique, afin de savoir où je me situe sans attendre un prof. | Léa Martin | 3  | S3     |
| US-05 | En tant qu'étudiant·e, je veux voir mon score /10 et le détail des bonnes et mauvaises réponses, afin de mesurer ma progression sur ce chapitre.  | Léa Martin | 3  | S3     |
| US-06 | En tant qu'étudiant·e, je veux consulter l'historique de mes quiz passés, afin de suivre mon évolution dans le temps.                             | Léa Martin | 3  | S4     |

Total MUST : 25 SP

### Traçabilité F1–F6

| Feature            | US    | Brownfield — état actuel                                                                              |
| ------------------ | ----- | ------------------------------------------------------------------------------------------------------- |
| F1 — Auth         | US-01 | Inscription, login, validation email implémentés. Doublon email non géré. Tests manquants.          |
| F2 — Upload       | US-02 | Upload PDF et saisie texte fonctionnels. Bug : PDF corrompu → HTTP 500 silencieux au lieu de HTTP 400. |
| F3 — Génération | US-03 | Génération 10 QCM via Ollama fonctionnelle. Timeout = 600 s (cible < 60 s). ADR-01 requis dès J2.    |
| F4 — Passage      | US-04 | Soumission des réponses fonctionnelle. Pas de tests d'intégration sur la persistance.                 |
| F5 — Score        | US-05 | Affichage score et correction fonctionnels. Distinction visuelle bonne/mauvaise réponse non testée.   |
| F6 — Historique   | US-06 | Endpoint /api/quizzes/ existe. Tri par date décroissante non garanti. Pagination non testée.          |

### Critères d'acceptation — MUST

#### US-01 — Créer un compte

- Given : un visiteur non authentifié sur /signup
- When : il soumet un email valide et un mot de passe d'au moins 8 caractères
- Then : POST /api/accounts/signup/ retourne HTTP 201, le compte est créé, un email de vérification est envoyé, la réponse contient un token d'accès — HTTP 400 avec message clair si l'email est déjà utilisé

#### US-02 — Uploader un PDF ou saisir un texte

- Given : un utilisateur authentifié sur /upload
- When : il dépose un PDF ≤ 5 Mo OU saisit un texte ≥ 200 caractères et valide
- Then : le contenu est extrait, stocké, le bouton "Générer un quiz" devient actif — HTTP 400 avec message lisible si le PDF est corrompu ou > 5 Mo (aucun HTTP 500 silencieux)

Note : bug brownfield prioritaire — pypdf lève une exception non interceptée sur les PDF malformés. À corriger avant la Review S1.

#### US-03 — Générer 10 QCM en moins de 60 s

- Given : un cours est soumis et le fournisseur LLM est actif (Llama 3.1 8B via Ollama, ou fournisseur retenu après ADR-01 à J2)
- When : l'utilisateur clique "Générer un quiz"
- Then : POST /api/llm/generate-quiz/ retourne HTTP 201 en moins de 60 s, avec 10 objets question (prompt + 4 options + correct\_index) — HTTP 504 avec message lisible si le délai est dépassé

Note : timeout actuel = 600 s, sans message d'erreur. L'ADR-01 (mardi matin) déclenchera soit un réglage du timeout Ollama, soit une bascule vers Groq ou un autre fournisseur.

#### US-04 — Soumettre les réponses et obtenir la correction

- Given : un quiz de 10 QCM est affiché sur /quiz/:id
- When : l'utilisateur sélectionne une réponse par question et soumet
- Then : POST /api/quizzes/:id/answer/ retourne HTTP 200, selected\_index est persisté pour chaque question, le statut bon/mauvais est enregistré, le score est calculé côté serveur

#### US-05 — Voir le score et le détail des réponses

- Given : les réponses ont été soumises
- When : l'utilisateur arrive sur la page résultat
- Then : le score /10 est affiché, chaque question affiche la bonne réponse en vert et, si applicable, la réponse erronée sélectionnée en rouge, un bouton "Refaire ce quiz" est disponible

#### US-06 — Consulter l'historique des quiz

- Given : un utilisateur authentifié a passé au moins un quiz
- When : il accède à /history
- Then : GET /api/quizzes/ retourne une liste paginée triée par date décroissante, chaque entrée affiche le titre du cours, la date, le score /10 et un lien "Refaire"

---

## SHOULD — Release 2, à livrer jeudi 3 juillet 17h

| ID    | User Story                                                                                                                                                    | Persona      | SP | Sprint          |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | -- | --------------- |
| US-07 | En tant qu'étudiant·e, je veux réinitialiser mon mot de passe par email (lien valide 1h), afin de ne pas être bloqué·e si je l'oublie.                  | Léa Martin  | 3  | S6              |
| US-08 | En tant qu'étudiant·e, je veux accéder à une bibliothèque de mes cours uploadés, afin de regénérer un quiz sur un support déjà soumis.              | Léa Martin  | 5  | si dispo S6–S7 |
| US-09 | En tant qu'étudiant·e, je veux choisir le niveau de difficulté et le nombre de questions (5–20), afin d'adapter la session à mon objectif de révision.  | Léa Martin  | 5  | S7              |
| US-10 | En tant qu'étudiant·e, je veux activer un timer optionnel par question (10–30 s), afin de simuler les conditions d'examen.                                 | Léa Martin  | 3  | S7              |
| US-11 | En tant qu'étudiant·e, je veux un dashboard de progression par chapitre, afin de savoir précisément où j'ai des lacunes avant les partiels.              | Léa Martin  | 5  | si dispo S7     |
| US-12 | En tant qu'utilisateur·trice, je veux exporter mes données (JSON + CSV, Art. 15 RGPD), afin d'exercer mon droit d'accès sans contacter le support.         | Tous         | 5  | S5              |
| US-22 | En tant qu'enseignante, je veux voir la progression de chaque étudiant·e (score moyen, dernier quiz, nombre de sessions), afin de cibler mes interventions. | Mme Lefèvre | 5  | S6              |

Total SHOULD : 31 SP

### Critères d'acceptation — SHOULD (résumés)

#### US-07 — Réinitialiser le mot de passe

Lien magique envoyé par email, valide 1h, redirige vers /reset-password/:token. Pas de confirmation si l'email est inconnu (anti-énumération RGPD).

#### US-08 — Bibliothèque de cours

/library liste les cours avec date d'upload, titre et nombre de quiz générés. Bouton "Regénérer un quiz" sur chaque entrée.

#### US-09 — Niveau de difficulté et nombre de questions

3 niveaux sélectionnables (Facile / Moyen / Difficile) et slider de 5 à 20 questions sur /quiz/new. Paramètres transmis au prompt LLM.

#### US-10 — Mode timer

Toggle ON/OFF sur la page quiz. Si actif : countdown configurable de 10 à 30 s par question. Réponse verrouillée à l'expiration du timer.

#### US-11 — Dashboard de progression

/dashboard affiche le score moyen par chapitre. Données disponibles dès le premier quiz. Chapitres en dessous de 5/10 signalés visuellement.

#### US-12 — Export RGPD Art. 15

Bouton "Exporter mes données" dans les paramètres du compte. Archive ZIP contenant quiz.json, reponses.csv, et audit.json (dates d'accès).

#### US-22 — Suivi classe enseignante (J1)

/teacher affiche la liste des étudiants avec score moyen, dernier quiz passé et nombre total de sessions. Accessible uniquement au compte enseignant.

---

## COULD — Si capacité disponible

| ID    | User Story                                                                                                                                                          | Persona      | SP | Cible            |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | -- | ---------------- |
| US-13 | En tant qu'étudiant·e, je veux me connecter via Google ou Apple (OAuth), afin de ne pas gérer un mot de passe supplémentaire.                                   | Léa Martin  | 5  | R2 si dispo      |
| US-14 | En tant qu'étudiant·e, je veux importer un cours depuis une URL web, afin de ne pas avoir à copier-coller l'article.                                             | Léa Martin  | 8  | R2 si dispo      |
| US-15 | En tant qu'enseignant·e, je veux générer des questions ouvertes corrigées par le LLM, afin de varier les modes d'évaluation.                                   | Mme Lefèvre | 13 | R2 si dispo      |
| US-16 | En tant qu'étudiant·e, je veux identifier mes lacunes par chapitre (agrégation des questions ratées), afin de planifier mes révisions.                         | Léa Martin  | 8  | R2 si dispo      |
| US-17 | En tant qu'utilisateur·trice, je veux supprimer mon compte et mes données (Art. 17 RGPD), afin d'exercer mon droit à l'effacement.                               | Tous         | 5  | R2 si dispo      |
| US-21 | En tant qu'enseignante, je veux voir la progression de mes étudiants depuis l'interface admin, afin d'avoir une visibilité sans développement front spécifique. | Mme Lefèvre | 2  | R1 si dispo (S4) |
| US-23 | En tant qu'enseignante, je veux envoyer un message d'encouragement à un·e étudiant·e depuis mon interface, afin d'intervenir sans sortir de la plateforme.      | Mme Lefèvre | 5  | R2 si dispo      |

Total COULD : 46 SP

### Critères d'acceptation — COULD (résumés)

#### US-13 — OAuth Google/Apple

Boutons de connexion sociale via django-allauth. Pas de création de mot de passe requise. Compte lié à l'email du provider.

#### US-14 — Import URL web

Champ URL sur /upload. Extraction du texte via scraping + filtrage des éléments parasites (nav, footer, publicités). Erreur lisible si l'URL est inaccessible ou bloquée.

#### US-15 — Questions ouvertes corrigées par LLM

Mode alternatif sur la génération de quiz. Le LLM évalue la réponse libre et retourne un barème indicatif + commentaire. Résultat clairement marqué comme "estimation IA".

#### US-16 — Identifier lacunes par chapitre

Agrégation des questions ratées (< 5/10 sur au moins 2 sessions). Tag "à retravailler" sur les chapitres concernés dans l'historique.

#### US-17 — Supprimer son compte (Art. 17 RGPD)

Bouton "Supprimer mon compte" dans les paramètres. Confirmation en 2 étapes (email + case à cocher). Purge complète des données sous 30 jours. Confirmation écrite envoyée par email.

#### US-21 — Vue progression via /admin (J1 R1)

L'interface Django Admin affiche déjà les modèles Quiz et User. Accorder un accès staff à Mme Lefèvre permet une visibilité sans développement front. 2 SP = configuration + documentation d'utilisation.

#### US-23 — Message enseignant vers étudiant (J1)

Formulaire sur /teacher/student/:id. Envoi par email (Brevo en prod, console.log en développement). Pas d'interface de réception intégrée en R2.

---

## WON'T — Hors scope semaine

| ID    | User Story                                                                                                                                   | Persona       | SP | Raison                                                             |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | -- | ------------------------------------------------------------------ |
| US-18 | En tant que DSI, je veux une authentification SSO entreprise SAML/OIDC, afin d'intégrer EduTutor dans l'annuaire de l'établissement.       | M. David Chen | 13 | B2B Release 3+ — intégration annuaire hors périmètre prototype |
| US-19 | En tant qu'étudiant·e, je veux un chatbot IA pour explorer un sujet par dialogue, afin d'approfondir mes révisions de façon interactive. | Léa Martin   | 21 | Positionnement concurrent de Khanmigo — hors vision quiz          |
| US-20 | En tant qu'étudiant·e, je veux participer à un mode compétition entre étudiants, afin de me motiver en révisant avec mes camarades.    | Léa Martin   | 13 | Hors vision individuelle — gamification à risque pédagogique    |

Total WON'T : 47 SP

---

## Récapitulatif du scope

| Priorité                     | Stories | SP | Livraison cible                             |
| ----------------------------- | ------- | -- | ------------------------------------------- |
| MUST                          | 6       | 25 | Release 1 — mercredi 17h45                 |
| SHOULD                        | 7       | 31 | Release 2 — jeudi 17h                      |
| COULD                         | 7       | 46 | Si capacité disponible                     |
| WON'T                         | 3       | 47 | Hors semaine                                |
| Total engagé (MUST + SHOULD) | 13      | 56 | Vélocité cible : 8 SP/sprint × 7 sprints |

---

## Perturbation J1 — Intégration de Mme Sophie Lefèvre

La perturbation J1 a été reçue le lundi matin, pendant la séance de cadrage.

Mme Sophie Lefèvre (42 ans, professeure BTS Communication, 28 étudiants, Lyon 6e) rejoint la story map en tant que persona secondaire et demande une interface enseignante. Elle n'a aucune story MUST — le parcours étudiant F1–F6 reste inchangé pour Release 1.

| Story J1                                    | Priorité | SP | Justification                                                                     |
| ------------------------------------------- | --------- | -- | --------------------------------------------------------------------------------- |
| US-21 — Vue admin progression              | COULD R1  | 2  | /admin Django suffit, 0 développement front — valeur démo forte si dispo en S4 |
| US-22 — Dashboard classe enseignante       | SHOULD R2 | 5  | Interface dédiée — valeur pédagogique réelle, réalisable en S6–S7          |
| US-23 — Messagerie enseignant → étudiant | COULD R2  | 5  | Différenciateur fort, mais risque scope creep si intégré trop tôt             |

Note de décision : la perturbation J1 est documentée et absorbée. Le scope MUST reste à 25 SP. US-22 est classée SHOULD et porte le scope engagé de 51 SP à 56 SP — aligné avec la vélocité cible de 7 sprints à 8 SP.

Raisonnement :

- US-21 est la seule story enseignante envisageable en Release 1 car elle réutilise /admin sans développement front spécifique.
- US-22 nécessite une page /teacher dédiée, cohérente avec une Release 2 planifiée en Sprint 6–7.
- US-23 (messagerie) est trop risquée en scope pour une semaine brownfield — classée COULD R2.

---

## Definition of Ready

Une story est prête à entrer dans un sprint quand :

- Elle est rédigée au format "En tant que... je veux... afin de..."
- Elle dispose de critères d'acceptation testables (Given / When / Then)
- Son estimation en story points est consensuelle
- Ses dépendances sont identifiées
- Elle est réalisable dans un seul sprint (split si > 8 SP)

---

## Definition of Done

Une story est terminée quand :

- Les critères d'acceptation sont vérifiés manuellement ou par tests automatisés
- Le code est pushé sur la branche main, CI verte
- La fonctionnalité est démontrée dans la Sprint Review
- Aucune régression sur les stories précédemment Done

---

## Auto-évaluation

| Critère                                                            | Statut | Remarque |
| ------------------------------------------------------------------- | ------ | -------- |
| Chaque story est au format INVEST                                   |        |          |
| Chaque story a un critère d'acceptation en Given/When/Then         |        |          |
| Les 6 stories MUST couvrent exactement F1–F6                       |        |          |
| La priorisation MoSCoW est justifiée par les personas              |        |          |
| La perturbation J1 est intégrée avec impact et décision          |        |          |
| Les WON'T sont documentés avec une raison explicite                |        |          |
| Le scope total MUST + SHOULD = 56 SP (vélocité 7 sprints × 8 SP) |        |          |
| Le document a été relu par l'équipe                              |        |          |
