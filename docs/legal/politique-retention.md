# Politique de rétention des données — EduTutor IA

## 1. Durées de conservation par type de donnée

| Donnée | Durée | Justification |
|---|---:|---|
| Compte utilisateur | Tant que le compte est actif | Nécessaire à la fourniture du service |
| Profil utilisateur | Tant que le compte est actif | Données complémentaires liées au compte |
| Cours importés (texte/PDF) | Tant que le quiz associé existe ou jusqu'à suppression du compte | Donnée source nécessaire au quiz |
| Quiz générés | Tant que le compte est actif ou jusqu'à suppression manuelle | Historique pédagogique de l'utilisateur |
| Réponses et scores | Tant que le quiz associé existe | Suivi de progression et de performance |
| Tokens d'authentification | Jusqu'à déconnexion, suppression ou rotation | Sécurité des sessions |
| Logs applicatifs (stdout) | 12 mois maximum | Sécurité et diagnostic — aligné aux bonnes pratiques CNIL |
| Signalements | 3 ans maximum | **À implémenter** — gestion des litiges et prescription civile |
| Demandes SAR / audit trail | 3 ans | **À implémenter** — preuve de conformité en cas de contrôle CNIL |
| Exports SAR temporaires | 30 jours maximum | Limitation du risque de fuite de données |

## 2. Motifs légaux (base RGPD Art. 6)

| Finalité | Base légale | Justification |
|---|---|---|
| Création et gestion du compte | Exécution du contrat (Art. 6.1.b) | L'utilisateur demande explicitement l'accès au service |
| Génération de quiz à partir des cours | Exécution du contrat (Art. 6.1.b) | Fonctionnalité centrale du service souscrit |
| Suivi pédagogique (scores, historique) | Exécution du contrat (Art. 6.1.b) | Permettre à l'utilisateur de suivre sa progression |
| Sécurité (logs, prévention des abus) | Intérêt légitime (Art. 6.1.f) | Protection du système et des utilisateurs |
| Réponse aux demandes RGPD (SAR) | Obligation légale (Art. 6.1.c) | Conformité au RGPD Art. 15 à 20 |
| Amélioration du service (stats agrégées) | Intérêt légitime (Art. 6.1.f) | Optimisation sans profilage individuel |
| Signalements | Obligation légale / Intérêt légitime | **À implémenter** — selon nature du signalement |

## 3. Modalités de suppression (Art. 17 RGPD — Droit à l'effacement)

### Suppression à la demande de l'utilisateur

- L'utilisateur peut demander la suppression de son compte via le bouton "Supprimer mon compte" dans les paramètres.
- La suppression est **définitive** (hard delete) et entraîne la suppression en cascade de :
  - profil utilisateur (`accounts_profile`)
  - quiz et questions (`quizzes_quiz`, `quizzes_question`)
  - tokens d'authentification
- Les logs applicatifs sont conservés pendant 12 mois pour des raisons de sécurité, mais désidentifiés si possible.

### Suppression automatique (durées expirées)

- Comptes inactifs depuis plus de 3 ans : suppression programmée après notification.
- Exports SAR temporaires : suppression automatique après 30 jours.
- Logs applicatifs : rotation automatique au-delà de 12 mois.

### Modalité technique

- Suppression via Django ORM avec `on_delete=CASCADE` sur les relations.
- Procédure manuelle pour les demandes SAR hors compte (à documenter).
- Cron ou tâche planifiée pour la purge automatique des durées expirées (à implémenter post-MVP).

---

*Document produit dans le cadre de la perturbation J3-bis — APOCAL'IPSSI 2026*
