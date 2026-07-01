# Definition of Done & Definition of Ready — EduTutor IA

---

## 1. Definition of Ready (DoR)

> Une User Story est **prête** à entrer dans un Sprint si elle satisfait **tous** les critères suivants.

### Checklist DoR

- [ ] La User Story est écrite selon le format : *"En tant que [persona], je veux [action] pour [bénéfice]"*
- [ ] Les critères d'acceptation sont rédigés, précis et testables (pas de formulation ambiguë)
- [ ] La User Story est estimée en Story Points par l'équipe (Planning Poker effectué)
- [ ] Les dépendances techniques sont identifiées et soit résolues, soit planifiées
- [ ] La User Story est indépendante d'une autre US non terminée dans le même sprint (ou la dépendance est explicitement acceptée)
- [ ] La maquette ou la description UX est disponible si la US implique une interface graphique
- [ ] La User Story peut être terminée en **un seul sprint** (sinon la décomposer)
- [ ] Le Product Owner a validé la priorité et le contenu

### Quand une US n'est PAS ready

- Les critères d'acceptation sont vagues ("le quiz doit être bon")
- L'US dépend d'un composant externe non encore livré
- L'estimation n'a pas été faite ou fait débat sans résolution
- La US est trop grande (> 13 SP — décomposer obligatoire)

---

## 2. Definition of Done (DoD)

> Une User Story est **terminée** (Done) si **tous** les critères suivants sont satisfaits. Aucune exception.

### 2.1 Code

- [ ] Le code est écrit, committé et pushé sur la branche feature correspondante (`feat/<slug>`)
- [ ] Le code respecte les conventions du projet (black/ruff pour Python, eslint/prettier pour TypeScript)
- [ ] Aucun `TODO` ou `FIXME` non documenté n'est laissé dans le code livré
- [ ] Le code est relu par au moins **un autre développeur** (Pull Request approuvée)
- [ ] Aucune clé API, mot de passe ou secret n'est commité dans le dépôt

### 2.2 Tests

- [ ] Des tests unitaires couvrent la logique métier de la US
- [ ] Tous les tests existants passent (aucune régression introduite)
- [ ] La couverture de tests n'a pas diminué par rapport au sprint précédent
- [ ] Le cas nominal **et** au moins un cas d'erreur sont testés

### 2.3 CI/CD

- [ ] La pipeline GitHub Actions est verte (lint + tests backend + tests frontend)
- [ ] Le code est mergé sur `main` via Pull Request (pas de push direct)
- [ ] Le message de commit respecte la convention Conventional Commits (`feat(scope): description`)

### 2.4 Fonctionnel

- [ ] La fonctionnalité a été testée manuellement par un membre de l'équipe différent du développeur
- [ ] Tous les critères d'acceptation de la US sont vérifiés et cochés
- [ ] Les cas limites identifiés lors du refinement ont été testés

### 2.5 Documentation

- [ ] Si la US modifie une API, le schéma OpenAPI est mis à jour (auto-généré par drf-spectacular)
- [ ] Si la US introduit une nouvelle variable d'environnement, elle est documentée dans `.env.example`
- [ ] Si la US modifie le comportement de déploiement, le guide de déploiement est mis à jour

### 2.6 Accessibilité & UX

- [ ] Les éléments interactifs ont des labels `aria-label` ou `aria-labelledby` corrects
- [ ] Les formulaires ont des messages d'erreur explicites et accessibles
- [ ] La fonctionnalité est utilisable au clavier (tabindex cohérent)

### 2.7 Sécurité

- [ ] Aucune donnée sensible n'est loguée ou exposée via l'API sans nécessité
- [ ] Les entrées utilisateur sont validées côté serveur (pas uniquement côté client)
- [ ] Les endpoints protégés vérifient bien l'authentification et les autorisations

---

## 3. DoD par niveau

### Niveau User Story (obligatoire)

Tous les critères des sections 2.1 à 2.7 ci-dessus.

### Niveau Sprint (Sprint Review)

- [ ] L'incrément est **déployable** (fonctionne en environnement de staging)
- [ ] Les US livrées sont démontrables au Product Owner et aux parties prenantes
- [ ] Le CHANGELOG.md est mis à jour avec les fonctionnalités livrées
- [ ] La dette technique introduite dans le sprint est documentée dans le backlog

### Niveau Release (production)

- [ ] Tous les tests passent en environnement de production
- [ ] Les pages légales sont complètes et publiées
- [ ] Le rate limiting est en place sur tous les endpoints critiques
- [ ] Les clés API sont chiffrées en base de données
- [ ] Le monitoring est actif et les alertes configurées
- [ ] Une revue de sécurité a été effectuée
- [ ] Les sauvegardes automatiques sont configurées et testées

---

## 4. Différence DoR / DoD en pratique

| Question | Réponse |
|----------|---------|
| **Qui** vérifie la DoR ? | Le Scrum Master avec le Product Owner, avant le Sprint Planning |
| **Quand** vérifie-t-on la DoR ? | Au Backlog Refinement et au début du Sprint Planning |
| **Qui** vérifie la DoD ? | L'équipe de développement, puis le Product Owner valide lors de la Sprint Review |
| **Quand** vérifie-t-on la DoD ? | À chaque clôture de tâche par le développeur, puis lors de la Sprint Review |
| **Que faire si une US n'est pas DoD à la fin du sprint ?** | Elle retourne dans le backlog, non démontrée, non comptabilisée dans la vélocité |

---

## 5. Exemples appliqués au projet

### Exemple — US-40 (Page Mentions Légales)

**DoR :**
- ✅ Format US respecté
- ✅ Critères : éditeur, hébergeur, directeur de publication mentionnés
- ✅ Estimée à 2 SP
- ✅ Template HTML disponible dans `frontend/src/pages/legal/`

**DoD :**
- ✅ Code committé + PR approuvée
- ✅ Contenu validé par le PO (ou responsable légal)
- ✅ Page accessible depuis le footer du site
- ✅ Lien de navigation fonctionnel dans `Layout.tsx`
- ✅ CI verte

### Exemple — US-50 (Rate Limiting)

**DoR :**
- ✅ Limites définies : 5 req/min/user sur generate-quiz, 10 req/min/IP sur login
- ✅ Estimée à 5 SP
- ✅ Bibliothèque choisie : `django-ratelimit` ou middleware custom

**DoD :**
- ✅ Rate limiting actif sur les endpoints ciblés
- ✅ HTTP 429 retourné avec message explicatif
- ✅ Test unitaire vérifiant le déclenchement du rate limit
- ✅ Pas de régression sur les tests existants
- ✅ Variable de configuration dans `.env.example`
