# Spécification — Audit trail des SAR (DataRequest)

## Objectif

Tracer chaque demande d'accès aux données (SAR — Subject Access Request) pour preuve de conformité CNIL et suivi des réponses RGPD Art. 15.

## Modèle proposé : `DataRequest`

### Champs

| Champ | Type | Description |
|---|---|---|
| `user` | ForeignKey → User | Utilisateur ayant formulé la demande |
| `requested_at` | DateTime (auto_now_add) | Date et heure de réception de la demande |
| `status` | CharField (choices) | Statut de traitement :
  - `received` — Reçue
  - `in_progress` — En cours de traitement
  - `completed` — Répondue |
| `responded_at` | DateTime (nullable) | Date et heure de la réponse effective |
| `file_hash` | CharField (64 car.) | Hash SHA-256 du fichier exporté (preuve d'intégrité) |

### Exemple d'enregistrement

```
DataRequest
  user: hugo.petit@test.local
  requested_at: 2026-07-01 10:30:00
  status: completed
  responded_at: 2026-07-01 14:15:00
  file_hash: a3f5c8e2d1... (SHA-256 du fichier JSON exporté)
```

## Procédure de mise à jour du statut

1. **Réception de la demande** → création avec statut `received`.
2. **Début du traitement** → passage à `in_progress`.
3. **Génération de l'export** → calcul du hash SHA-256 du fichier.
4. **Envoi de la réponse** → passage à `completed`, enregistrement de `responded_at` et `file_hash`.

## Utilisation du hash

- Le hash SHA-256 est calculé sur le contenu brut de l'export (JSON ou CSV).
- Il permet de prouver qu'un fichier n'a pas été altéré entre génération et transmission.
- En cas de litige, le hash stocké en base fait foi de l'intégrité de la réponse.

## Règles de sécurité

- Un utilisateur ne peut voir que **ses propres** `DataRequest` (filtrage par `user`).
- L'administrateur peut consulter l'ensemble pour supervision conformité.
- Aucune modification manuelle du hash après enregistrement.

## Statut d'implémentation

**À implémenter** — modèle et logique prêts, migration et intégration à l'endpoint export planifiées post-MVP.
