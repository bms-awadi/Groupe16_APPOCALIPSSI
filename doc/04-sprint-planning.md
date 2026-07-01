# Sprint Planning — EduTutor IA

> **Vélocité estimée** : 30 Story Points / sprint  
> **Durée des sprints** : 2 semaines  
> **Taille de l'équipe** : 4–5 développeurs  
> **Période** : Juillet – Octobre 2026

---

## Vue d'ensemble des sprints

| Sprint | Période | Thème | SP Planifiés | US incluses |
|--------|---------|-------|-------------|------------|
| Sprint 1 | 30 juin – 11 juil. 2026 | Stabilisation & Tests | 30 SP | US-60, US-61, US-14, US-53, US-54 |
| Sprint 2 | 14 – 25 juil. 2026 | Conformité Légale & Sécurité | 31 SP | US-40, US-41, US-42, US-43, US-44, US-50, US-51 |
| Sprint 3 | 28 juil. – 8 août 2026 | UX, Qualité & Fonctionnalités | 30 SP | US-62, US-52, US-34, US-21, US-22, US-16 |
| Sprint 4 | 11 – 22 août 2026 | Déploiement & Monitoring | 26 SP | US-70, US-71, US-72, US-73, US-35 |

---

## SPRINT 1 — Stabilisation & Tests

**Période** : 30 juin – 11 juillet 2026  
**Objectif du sprint** : Sécuriser la base de code existante par des tests complets et corriger les comportements imprévisibles identifiés.

### Sprint Goal

> *"À la fin de ce sprint, l'équipe dispose d'une suite de tests fiable sur le frontend et le backend, et les comportements anormaux (tokens expirés, PDF corrompu) sont gérés proprement."*

### User Stories du Sprint 1

| ID | User Story | SP | Assigné à |
|----|-----------|-----|----------|
| US-60 | Tests unitaires frontend (UploadPage, QuizPage, HistoryPage, LoginPage, SignupPage) | 13 | Dev Frontend 1 + 2 |
| US-61 | Tests d'intégration flux principal (inscription → quiz → résultat) | 8 | Dev Backend |
| US-14 | Recherche/filtre dans l'historique des quiz | 3 | Dev Frontend 1 |
| US-53 | Expiration des tokens email (vérification 48h, reset 1h) | 3 | Dev Backend |
| US-54 | Gestion des erreurs PDF sans plantage silencieux | 3 | Dev Backend |
| **Total** | | **30** | |

### Tâches techniques Sprint 1

#### US-60 — Tests unitaires frontend
- [ ] Setup vitest + testing-library si non configuré
- [ ] Tests `LoginPage` : formulaire valide, erreur identifiants, redirect post-login
- [ ] Tests `SignupPage` : validation email, mot de passe faible, succès
- [ ] Tests `UploadPage` : upload PDF (mock), saisie texte, validation
- [ ] Tests `QuizPage` : affichage 10 questions, soumission, affichage score
- [ ] Tests `HistoryPage` : liste vide, liste avec items, pagination
- [ ] Configurer le rapport de couverture dans `package.json`

#### US-61 — Tests d'intégration
- [ ] Configurer `pytest` avec fixtures de base de données de test
- [ ] Test flux complet : signup → login → generate-quiz (mock LLM) → answer → score
- [ ] Test flux reset password : request → email → confirm → login
- [ ] Ajouter ces tests au pipeline CI (job dédié)

#### US-14 — Recherche dans l'historique
- [ ] Ajouter un champ de recherche dans `HistoryPage.tsx`
- [ ] Filtrage côté client sur le titre du quiz (simple, sans appel API)
- [ ] OU ajouter un paramètre `?search=` au endpoint `GET /api/quizzes/`
- [ ] Afficher "Aucun résultat" si la recherche ne trouve rien

#### US-53 — Expiration des tokens email
- [ ] Implémenter `PasswordResetToken` avec champ `expires_at` (now + 1h)
- [ ] Implémenter expiration du token de vérification email (48h)
- [ ] Retourner HTTP 400 + message clair si token expiré
- [ ] Ajouter tests unitaires sur l'expiration

#### US-54 — Gestion erreurs PDF
- [ ] Entourer l'extraction pypdf d'un try/except spécifique
- [ ] Retourner HTTP 400 avec message "PDF illisible ou corrompu"
- [ ] Logger l'erreur côté serveur (exception + nom de fichier)
- [ ] Tester avec un PDF corrompu en test unitaire

### Critères d'acceptation du Sprint 1

- La CI passe en vert avec les nouveaux tests
- La couverture frontend atteint ≥ 70 % sur les 5 pages testées
- Les flux d'intégration passent sans mock LLM externe (backend = mock)
- Un PDF corrompu retourne une erreur 400 (pas un 500)
- Un token de reset expiré retourne une erreur explicite

### Impediments potentiels Sprint 1

| Risque | Probabilité | Impact | Mitigation |
|--------|------------|--------|-----------|
| Configuration vitest difficile | Moyenne | Moyen | Utiliser le fichier `errors.test.ts` existant comme modèle |
| Tests flaky (dépendant du temps) | Haute | Élevé | Mocker les appels de temps (`Date.now`) |
| Scope trop large pour les tests | Haute | Élevé | Prioriser les 3 pages les plus critiques d'abord |

---

## SPRINT 2 — Conformité Légale & Sécurité

**Période** : 14 – 25 juillet 2026  
**Objectif du sprint** : Mettre l'application en conformité légale (RGPD) et sécuriser les vecteurs d'attaque les plus évidents.

### Sprint Goal

> *"À la fin de ce sprint, toutes les pages légales sont publiées, les clés API sont chiffrées, et aucun endpoint critique ne peut être abusé par du spam."*

### User Stories du Sprint 2

| ID | User Story | SP | Assigné à |
|----|-----------|-----|----------|
| US-40 | Page Mentions Légales | 2 | Dev Frontend |
| US-41 | Page Politique de Confidentialité | 3 | Dev Frontend + PO (contenu) |
| US-42 | Page CGU | 3 | Dev Frontend + PO (contenu) |
| US-43 | Page Politique de Cookies | 2 | Dev Frontend |
| US-44 | Droits RGPD — contact DPD visible | 2 | Dev Frontend |
| US-50 | Rate Limiting sur endpoints critiques | 5 | Dev Backend |
| US-51 | Chiffrement des clés API LLM | 8 | Dev Backend |
| Refactoring | Mise à jour `.env.example` avec nouvelles variables | 2 | DevOps |
| Refactoring | Revue de sécurité du code existant | 4 | Tous |
| **Total** | | **31** | |

### Tâches techniques Sprint 2

#### US-40 à US-43 — Pages légales
- [ ] Rédiger le contenu de chaque page (PO valide le contenu juridique)
- [ ] Remplir les composants React dans `frontend/src/pages/legal/`
- [ ] Vérifier les liens depuis le footer (`Layout.tsx`)
- [ ] S'assurer que les pages sont indexables (pas de `noindex`)

#### US-50 — Rate Limiting
- [ ] Installer `django-ratelimit` (ou middleware custom)
- [ ] Appliquer `@ratelimit(key='user', rate='5/m')` sur `generate-quiz`
- [ ] Appliquer `@ratelimit(key='ip', rate='10/m')` sur `login`
- [ ] Retourner HTTP 429 avec `Retry-After` header
- [ ] Tester le déclenchement du rate limit
- [ ] Documenter la configuration dans `.env.example`

#### US-51 — Chiffrement clés API
- [ ] Choisir la méthode : `cryptography.fernet` (recommandé)
- [ ] Créer un `EncryptedCharField` Django custom ou utiliser `django-encrypted-model-fields`
- [ ] Migrer le champ `api_keys` de `LLMConfig` pour chiffrer à la sauvegarde
- [ ] Vérifier que les clés ne sont jamais retournées en clair via l'API admin
- [ ] Stocker `FIELD_ENCRYPTION_KEY` dans `.env` et la documenter
- [ ] Tester la sauvegarde et la lecture d'une clé API

### Critères d'acceptation du Sprint 2

- Les 4 pages légales sont accessibles et contiennent du contenu réel
- Un email de contact DPD est visible dans la politique de confidentialité
- Un appel > 5 req/min sur generate-quiz retourne HTTP 429
- Les clés API dans la base de données sont illisibles sans la clé de chiffrement
- L'API admin ne retourne jamais une clé API en clair

---

## SPRINT 3 — UX, Qualité & Fonctionnalités

**Période** : 28 juillet – 8 août 2026  
**Objectif du sprint** : Améliorer l'expérience utilisateur, l'accessibilité, et livrer les fonctionnalités de suivi avancées.

### Sprint Goal

> *"À la fin de ce sprint, l'application est accessible WCAG AA sur les pages principales, le dashboard de progression est complet, et les admins disposent des logs d'activité."*

### User Stories du Sprint 3

| ID | User Story | SP | Assigné à |
|----|-----------|-----|----------|
| US-62 | Audit accessibilité WCAG AA + corrections | 8 | Dev Frontend |
| US-52 | Logs structurés (format JSON, endpoint admin) | 5 | Dev Backend |
| US-34 | Logs d'activité pour les admins | 8 | Dev Backend |
| US-21 | Graphique de progression (courbe score dans le temps) | 5 | Dev Frontend |
| US-22 | Indicateur de niveau utilisateur | 5 | Dev Frontend |
| **Total** | | **31** | |

> Si la vélocité le permet : ajouter US-16 (Export PDF des résultats, 8 SP)

### Tâches techniques Sprint 3

#### US-62 — Accessibilité WCAG AA
- [ ] Installer `@axe-core/react` pour détection automatique en dev
- [ ] Auditer les 5 pages principales (Login, Upload, Quiz, History, Dashboard)
- [ ] Corriger les erreurs de contraste (ratio ≥ 4.5:1)
- [ ] Ajouter `aria-label` sur les boutons icône
- [ ] Vérifier la navigation clavier (focus visible, ordre logique)
- [ ] Corriger les labels de formulaire manquants

#### US-52 — Logs structurés
- [ ] Configurer `python-json-logger` dans les settings Django
- [ ] Logger : authentification (login/logout), génération de quiz, erreurs 4xx/5xx
- [ ] Format : `{ timestamp, level, user_id, action, endpoint, ip, status_code }`
- [ ] Rotation des fichiers de log (max 50 Mo, 7 jours)

#### US-34 — Logs d'activité admin
- [ ] Créer un endpoint `GET /api/admin/activity-logs/`
- [ ] Filtres : par date, par user_id, par action
- [ ] Afficher dans l'interface admin (6e onglet)
- [ ] Pagination (25 entrées par page)

#### US-21/22 — Dashboard progression
- [ ] Intégrer `recharts` ou `chart.js` pour le graphique
- [ ] Endpoint `GET /api/quizzes/stats/` : scores dans le temps
- [ ] Calcul du niveau : Débutant (moy < 5), Intermédiaire (5-7), Expert (> 7)
- [ ] Afficher le badge de niveau sur le Dashboard

### Critères d'acceptation du Sprint 3

- Zéro erreur WCAG AA sur les 5 pages principales (axe-core)
- Les logs sont écrits en JSON et consultables
- Les admins voient un historique d'activité paginé et filtrable
- Le graphique de progression s'affiche après ≥ 3 quiz
- Le badge de niveau est affiché sur le Dashboard

---

## SPRINT 4 — Déploiement & Monitoring

**Période** : 11 – 22 août 2026  
**Objectif du sprint** : Mettre l'application en production avec HTTPS, sauvegardes et alertes.

### Sprint Goal

> *"À la fin de ce sprint, l'application est accessible en production via HTTPS, avec un monitoring actif et des sauvegardes quotidiennes automatisées."*

### User Stories du Sprint 4

| ID | User Story | SP | Assigné à |
|----|-----------|-----|----------|
| US-70 | Déploiement production VPS OVH | 8 | DevOps |
| US-71 | Monitoring + alertes uptime | 5 | DevOps |
| US-72 | Sauvegardes automatiques PostgreSQL | 5 | DevOps |
| US-73 | Pipeline CD (auto-deploy sur push main) | 8 | DevOps + Dev Backend |
| US-35 | Alerte admin si LLM inaccessible | 5 | Dev Backend |
| **Total** | | **31** | |

### Tâches techniques Sprint 4

#### US-70 — Déploiement production
- [ ] Provisionner le VPS OVH (Ubuntu 22.04, 4 vCPU, 8 Go RAM)
- [ ] Configurer le DNS (domaine → IP VPS)
- [ ] Déployer avec `docker-compose.prod.yml`
- [ ] Configurer Caddy (HTTPS automatique Let's Encrypt)
- [ ] Définir toutes les variables d'environnement de prod
- [ ] Lancer les migrations et le seed initial
- [ ] Vérifier `/health` en HTTPS

#### US-71 — Monitoring
- [ ] Créer un compte Uptime Robot (gratuit)
- [ ] Monitorer `/health` toutes les 5 minutes
- [ ] Configurer les alertes email (down → alerte immédiate)
- [ ] Documenter le tableau de bord de monitoring

#### US-72 — Sauvegardes
- [ ] Script `backup-postgres.sh` : `pg_dump` → fichier horodaté
- [ ] Cron quotidien à 3h00 sur le VPS
- [ ] Rotation automatique (garde 7 jours)
- [ ] Test de restauration documenté

#### US-73 — Pipeline CD
- [ ] Configurer `SSH_PRIVATE_KEY` dans les Secrets GitHub
- [ ] Job GitHub Actions : SSH sur VPS → `git pull` → `docker compose up -d`
- [ ] Rollback : tag Git `v<version>` + procédure documentée

#### US-35 — Alerte LLM inaccessible
- [ ] Tâche cron Django (ou Celery beat) qui ping le LLM toutes les 10 min
- [ ] Si 3 échecs consécutifs → email d'alerte à l'admin
- [ ] Indicateur de statut dans le Dashboard admin

### Critères d'acceptation du Sprint 4

- L'URL de production répond en HTTPS avec certificat valide
- Uptime Robot surveille l'application et les alertes sont configurées
- Un backup PostgreSQL est créé chaque nuit et conservé 7 jours
- Un push sur `main` déclenche un déploiement automatique (après CI)
- L'admin reçoit un email si le LLM est inaccessible depuis > 30 minutes

---

## Tableau de bord Sprints

```
Sprint 1 [Stabilisation & Tests]    █████████████████░░░░░░░░░░░░░░  30/30 SP
Sprint 2 [Légal & Sécurité]         ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  0/31 SP
Sprint 3 [UX & Fonctionnalités]     ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  0/31 SP
Sprint 4 [Déploiement & Monitoring] ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  0/31 SP
```

---

## Gestion de la vélocité

| Événement | Impact sur la vélocité | Action |
|-----------|----------------------|--------|
| Absence d'un membre | -6 SP par personne/sprint | Réduire le scope du sprint, informer le PO |
| US sous-estimée | Débordement possible | Déplacer les US basses priorité au sprint suivant |
| Blocage technique | Peut consommer 2-3 jours | Escalader au SM, chercher une alternative |
| CI bloquée | Impossible de merger | Prioriser la résolution, tout l'équipe s'y met |
