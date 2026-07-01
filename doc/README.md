# Documentation Gestion de Projet — EduTutor IA

Dossier de gestion de projet Agile Scrum pour le projet **EduTutor IA** (Groupe 16 – IPSSI).

---

## Documents disponibles

| # | Document | Description |
|---|----------|-------------|
| [00](./00-contexte-vision.md) | **Contexte & Vision** | Vision du produit, objectifs SMART, périmètre, contraintes |
| [01](./01-parties-prenantes-personas.md) | **Parties Prenantes & Personas** | Équipe Scrum, stakeholders, 4 personas utilisateurs |
| [02](./02-product-backlog.md) | **Product Backlog** | 35 User Stories réparties en 8 Épics, estimées en SP (MoSCoW) |
| [03](./03-definition-of-done-ready.md) | **DoD & DoR** | Critères de prêt et de terminé, exemples appliqués |
| [04](./04-sprint-planning.md) | **Sprint Planning** | Détail des 4 sprints (tâches, assignations, critères d'acceptation) |
| [05](./05-roadmap.md) | **Roadmap Produit** | Timeline, jalons, releases v1.3 → v2.0, KPIs |
| [06](./06-ceremonies-scrum.md) | **Cérémonies Scrum** | Templates Daily, Sprint Review, Rétrospective, Refinement |
| [07](./07-tableau-kanban.md) | **Tableau Kanban** | Statut des US, burndown, vélocité, ADR, working agreement |
| [08](./08-release-planning.md) | **Release Planning** | 4 releases (v1.3→v2.0), critères de sortie, procédures déploiement, rollback |

---

## État du projet à la reprise (juin 2026)

```text
État général : MVP1 + MVP2 livrés — reprise avec lacunes à combler
Story Points livrés : 58 / 185 SP total
SP restants à livrer : 127 SP (4 sprints de ~30 SP)
```

### Ce qui est terminé

- Authentification complète (signup, login, reset, vérification email)
- Génération de quiz via LLM (9 fournisseurs : Ollama, OpenAI, Claude, Gemini...)
- Prise de quiz, notation et historique
- Interface d'administration (config LLM, site, utilisateurs)
- Dashboard et revue des erreurs (MVP2)

### Ce qui reste à faire (priorité haute)

1. **Tests** — Couverture frontend quasi inexistante
2. **Conformité légale** — 4 pages légales vides (RGPD non respecté)
3. **Sécurité** — Rate limiting absent, clés API en clair en base
4. **Déploiement** — Jamais déployé en production

---

## Liens vers la documentation technique

La documentation technique du projet se trouve dans le dossier [`docs/`](../docs/) :

- Architecture : `docs/01-architecture.md`
- Déploiement : `docs/11-deploiement-vps-ovh.md`
- Guide étudiant : `GUIDE-ETUDIANT.md`
- Contribution : `CONTRIBUTING.md`

---

Documents créés le 29 juin 2026 — Groupe 16 IPSSI
