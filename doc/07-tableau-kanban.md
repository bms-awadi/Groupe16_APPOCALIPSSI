# Tableau Kanban & Suivi — EduTutor IA

---

## Structure du tableau Kanban

Le tableau comporte **5 colonnes** :

```
┌──────────────┬──────────────┬──────────────┬──────────────┬──────────────┐
│   BACKLOG    │   TO DO      │ IN PROGRESS  │   REVIEW     │    DONE      │
│  (prioritisé)│  (sprint)    │  (en cours)  │  (PR ouverte)│  (DoD ✅)   │
├──────────────┼──────────────┼──────────────┼──────────────┼──────────────┤
│              │              │   WIP: 1-2   │   WIP: 1-2   │              │
│  US-16       │  US-60       │  US-14       │  US-53       │  US-01 ✅    │
│  US-22       │  US-61       │              │              │  US-02 ✅    │
│  US-34       │  US-53       │              │              │  US-03 ✅    │
│  US-35       │  US-54       │              │              │  US-04 ✅    │
│  US-52       │              │              │              │  US-05 ✅    │
│  ...         │              │              │              │  US-06 ✅    │
│              │              │              │              │  US-07 ✅    │
│              │              │              │              │  US-10 ✅    │
│              │              │              │              │  US-11 ✅    │
│              │              │              │              │  US-12 ✅    │
│              │              │              │              │  US-13 ✅    │
│              │              │              │              │  US-15 ✅    │
│              │              │              │              │  US-20 ✅    │
│              │              │              │              │  US-30 ✅    │
│              │              │              │              │  US-31 ✅    │
│              │              │              │              │  US-32 ✅    │
│              │              │              │              │  US-33 ✅    │
└──────────────┴──────────────┴──────────────┴──────────────┴──────────────┘
```

> **WIP Limit** : Maximum 2 US "In Progress" simultanément pour limiter le multitâche et favoriser la complétion.

---

## Sprint 1 — Tableau détaillé

**Sprint Goal** : *"À la fin de ce sprint, l'équipe dispose d'une suite de tests fiable et les comportements anormaux sont gérés proprement."*

| US | Titre | SP | Assigné | Statut |
|----|-------|----|---------|--------|
| US-60 | Tests unitaires frontend | 13 | Dev 1 + Dev 2 | ⬜ TO DO |
| US-61 | Tests d'intégration flux principal | 8 | Dev 3 | ⬜ TO DO |
| US-14 | Recherche dans l'historique | 3 | Dev 1 | ⬜ TO DO |
| US-53 | Expiration des tokens email | 3 | Dev 3 | ⬜ TO DO |
| US-54 | Gestion erreurs PDF | 3 | Dev 3 | ⬜ TO DO |
| **Total** | | **30** | | |

### Burndown Sprint 1 (mise à jour quotidienne)

```
SP restants
30 │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
27 │
24 │
21 │
18 │
15 │
12 │
 9 │
 6 │
 3 │
 0 │────────────────────────────────
   J1  J2  J3  J4  J5  J6  J7  J8  J9  J10
```

> Mettre à jour ce graphique chaque jour au Daily Scrum.  
> Ligne idéale : décroissance de 3 SP/jour.

---

## Sprint 2 — Tableau détaillé

| US | Titre | SP | Assigné | Statut |
|----|-------|----|---------|--------|
| US-40 | Page Mentions Légales | 2 | Dev Frontend | ⬜ TO DO |
| US-41 | Page Politique de Confidentialité | 3 | Dev Frontend | ⬜ TO DO |
| US-42 | Page CGU | 3 | Dev Frontend | ⬜ TO DO |
| US-43 | Page Cookies | 2 | Dev Frontend | ⬜ TO DO |
| US-44 | Droits RGPD — contact DPD | 2 | Dev Frontend | ⬜ TO DO |
| US-50 | Rate Limiting | 5 | Dev Backend | ⬜ TO DO |
| US-51 | Chiffrement clés API | 8 | Dev Backend | ⬜ TO DO |
| Refactoring | `.env.example` + revue sécurité | 6 | Tous | ⬜ TO DO |
| **Total** | | **31** | | |

---

## Suivi de la vélocité

| Sprint | SP Planifiés | SP Livrés | Vélocité réelle | Écart |
|--------|-------------|-----------|----------------|-------|
| Héritage (MVP1+2) | — | 58 SP | — | — |
| Sprint 1 | 30 | — | — | — |
| Sprint 2 | 31 | — | — | — |
| Sprint 3 | 31 | — | — | — |
| Sprint 4 | 31 | — | — | — |
| **Total projet** | **123** | **58 (livrés)** | — | — |

---

## Suivi des impediments

| Date | Impediment | Soulevé par | Propriétaire | Statut | Date résolution |
|------|-----------|------------|-------------|--------|----------------|
| — | — | — | SM | — | — |

> Ajouter chaque impediment ici dès qu'il est soulevé au Daily Scrum.

---

## Suivi des décisions techniques (ADR)

Les décisions d'architecture importantes sont documentées ici avec leur contexte.

| # | Décision | Alternatives rejetées | Raison | Sprint |
|---|----------|----------------------|--------|--------|
| ADR-01 | Utiliser `cryptography.fernet` pour chiffrer les clés API | AES manuel, `django-encrypted-model-fields` | Fernet inclut IV + HMAC, simple à utiliser, bien maintenu | Sprint 2 |
| ADR-02 | Filtrage historique côté client (pas appel API) | Paramètre `?search=` sur l'endpoint | Nombre de quiz par user < 100, latence négligeable, plus simple | Sprint 1 |
| ADR-03 | `django-ratelimit` pour le rate limiting | Middleware custom, `drf-throttling` | Intégré avec DRF, configurable par clé (user/IP/header) | Sprint 2 |

---

## Matrice de compétences de l'équipe

> Utile pour l'assignation des tâches et identifier les besoins de montée en compétences.

| Compétence | Dev 1 | Dev 2 | Dev 3 | Dev 4 | Dev 5 |
|-----------|-------|-------|-------|-------|-------|
| Django / DRF | ★★★ | ★★☆ | ★★★ | ★☆☆ | ★★☆ |
| React / TypeScript | ★★★ | ★★★ | ★★☆ | ★★★ | ★☆☆ |
| Tests (pytest/vitest) | ★★☆ | ★★☆ | ★★☆ | ★☆☆ | ★☆☆ |
| Docker / DevOps | ★★☆ | ★☆☆ | ★★☆ | ★★★ | ★★☆ |
| Sécurité | ★★☆ | ★☆☆ | ★★★ | ★☆☆ | ★☆☆ |
| Accessibilité | ★☆☆ | ★★☆ | ★☆☆ | ★☆☆ | ★★☆ |

> ★★★ = Autonome | ★★☆ = Confirmé | ★☆☆ = En apprentissage

*Mettre à jour cette matrice à chaque sprint.*

---

## Règles d'équipe (Team Working Agreement)

Décidées lors du premier Sprint Planning :

1. **Heures de travail** : Core hours 9h–17h, réponses Slack sous 2h pendant ces heures
2. **Daily Scrum** : Chaque matin à 9h30, 15 min max, par Slack si remote
3. **PR** : Toute PR doit être relue par au moins 1 autre dev avant merge, dans les 24h
4. **Branches** : Format `feat/<scope>/<slug>`, supprimer après merge
5. **Commits** : Conventional Commits obligatoire (`feat(scope): description`)
6. **Secrets** : JAMAIS de clé API, mot de passe ou `.env` commité (pre-commit hook actif)
7. **Bugs critiques** : Escalader au SM dans le même Daily Scrum, ne pas attendre
8. **Rétrospective** : Bienveillance obligatoire — on critique les processus, pas les personnes
9. **Definition of Done** : Tous les critères DOIVENT être satisfaits avant de déplacer une US en Done
10. **Absence** : Prévenir le SM la veille si possible, mettre à jour son Daily en asynchrone
