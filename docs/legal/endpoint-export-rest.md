# Spécification — Endpoint d'export REST RGPD

## Endpoint

```
GET /api/accounts/me/export/?format=json|csv
```

## Objectif

Exporter l'intégralité des données personnelles de l'utilisateur authentifié, conformément à l'article 15 du RGPD.

## Authentification

- Token DRF requis dans le header `Authorization: Token <token>`.
- Réponse `401` si non authentifié.

## Paramètres de requête

| Paramètre | Valeurs | Défaut | Description |
|---|---|---|---|
| `format` | `json`, `csv` | `json` | Format de l'export |

## Données exportées (filtrage strict par `request.user`)

| Catégorie | Données | Source BDD |
|---|---|---|
| Compte utilisateur | email, username, prénom, nom, date de création, date de modification | `auth_user` |
| Profil | email vérifié, date de création du profil | `accounts_profile` |
| Cours importés | texte source, titre, dates | `quizzes_quiz` |
| Quiz générés | questions, options, index correct, score | `quizzes_question` |
| Réponses | réponse sélectionnée (selected_index) | `quizzes_question.selected_index` |
| Demandes SAR | historique des demandes d'accès (audit trail) | `accounts_datarequest` |

## Règle de sécurité critique

> **Filtrage obligatoire par `request.user`** — interdiction absolue d'utiliser `Model.objects.all()` ou tout autre requête non filtrée. Toute donnée d'un autre utilisateur dans l'export constitue une fuite de données.

## Formats de sortie

### JSON (défaut)

- Structure hiérarchique : `user`, `quizzes[]`, `data_requests[]`.
- `Content-Type: application/json`
- Nom de fichier : `edututor_export_<email>_<timestamp>.json`
- Header `Content-Disposition: attachment`

### CSV (bonus)

- Format aplati avec colonnes : `category, id, email, title, question_index, prompt, options, correct_index, selected_index, score, created_at`.
- `Content-Type: text/csv`
- Nom de fichier : `edututor_export_<email>_<timestamp>.csv`

## Intégrité

- Hash SHA-256 du contenu de l'export calculé avant envoi.
- Hash stocké dans l'audit trail `DataRequest` pour preuve de réponse.

## Erreurs

| Code | Cas |
|---|---|
| 400 | Format invalide (`?format=xml` par exemple) |
| 401 | Utilisateur non authentifié |
| 403 | Email non vérifié (si contrôle activé) |

## Statut d'implémentation

**À implémenter** — spécification prête, développement planifié post-MVP.
