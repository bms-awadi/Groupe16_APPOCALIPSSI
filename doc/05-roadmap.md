# Roadmap Produit — EduTutor IA

> Vue macroscopique de l'évolution du produit sur 4 mois.  
> Les sprints détaillés sont dans `04-sprint-planning.md`.

---

## Timeline

```
JUIN 2026              JUILLET 2026                AOÛT 2026            SEPT 2026
     │                      │                           │                    │
─────┼──────────────────────┼───────────────────────────┼────────────────────┼─────
     │                      │                           │                    │
[Reprise]           [S1]──────[S2]──────[S3]──────[S4]────────[Release]   [Suivi]
     │               │         │          │          │              │          │
 Analyse          Tests &   Légal &    UX &       Deploy &       v2.0.0    Monitoring
 Backlog         Stabilité  Sécurité   Qualité    Monitoring     PROD      & Retour
     │               │         │          │          │              │
  30 juin      11 juil.    25 juil.    8 août    22 août       fin août
```

---

## Jalons clés

| Jalon | Date cible | Critère de réussite |
|-------|-----------|---------------------|
| **M0 — Reprise du projet** | 30 juin 2026 | Analyse complète, backlog rédigé, équipe constituée |
| **M1 — Base stabilisée** | 11 juillet 2026 | CI verte, couverture tests ≥ 70 %, gestion erreurs PDF |
| **M2 — Conformité légale** | 25 juillet 2026 | 4 pages légales publiées, rate limiting actif, clés API chiffrées |
| **M3 — UX complète** | 8 août 2026 | WCAG AA, dashboard avancé, logs d'activité |
| **M4 — Production** | 22 août 2026 | HTTPS live, monitoring, sauvegardes, CD pipeline |
| **Release v2.0.0** | Fin août 2026 | Application complète en production, zéro blocant |

---

## Releases

### v1.2.0 (existante — code repris)

**Date** : Avant reprise  
**Statut** : ✅ Livrée

- Interface d'administration complète (5 onglets)
- Support multi-LLM (9 fournisseurs)
- Dashboard utilisateur (stats de base)
- Mode sombre
- Revue des erreurs

---

### v1.3.0 — Stabilisation

**Sprint** : Sprint 1  
**Date prévue** : 11 juillet 2026  
**Statut** : ⬜ À livrer

**Fonctionnalités** :
- Tests unitaires frontend sur 5 pages critiques
- Tests d'intégration flux principal
- Recherche dans l'historique des quiz
- Gestion des tokens expirés (email, reset)
- Gestion robuste des PDF corrompus

**Breaking changes** : Aucun (améliorations internes uniquement)

---

### v1.4.0 — Conformité & Sécurité

**Sprint** : Sprint 2  
**Date prévue** : 25 juillet 2026  
**Statut** : ⬜ À livrer

**Fonctionnalités** :
- Pages légales complètes (Mentions Légales, Confidentialité, CGU, Cookies)
- Rate limiting sur les endpoints critiques
- Chiffrement des clés API en base de données
- Contact DPD visible

**Breaking changes** :
- Variable d'environnement `FIELD_ENCRYPTION_KEY` **obligatoire** en production
- Migration de base de données pour le chiffrement (exécuter `migrate`)

---

### v1.5.0 — UX & Qualité

**Sprint** : Sprint 3  
**Date prévue** : 8 août 2026  
**Statut** : ⬜ À livrer

**Fonctionnalités** :
- Conformité WCAG AA sur les 5 pages principales
- Logs structurés (JSON)
- Logs d'activité dans l'interface admin
- Graphique de progression temporelle
- Badge de niveau utilisateur

**Breaking changes** : Aucun

---

### v2.0.0 — Production Ready

**Sprint** : Sprint 4  
**Date prévue** : 22 août 2026  
**Statut** : ⬜ À livrer

**Fonctionnalités** :
- Déploiement sur VPS OVH avec HTTPS
- Monitoring uptime (Uptime Robot)
- Sauvegardes PostgreSQL quotidiennes
- Pipeline CD (auto-déploiement)
- Alertes admin si LLM inaccessible

**Breaking changes** :
- Passer au backend LLM cloud (OpenAI, Groq, etc.) pour la production si pas de GPU
- Configuration Caddy requise (voir `docs/11-deploiement-vps-ovh.md`)

---

## Fonctionnalités futures (Backlog post-v2.0.0)

Ces fonctionnalités sont dans le backlog mais ne seront pas traitées dans cette phase du projet :

| Fonctionnalité | Valeur | Complexité | Priorité future |
|---------------|--------|-----------|-----------------|
| Export des résultats en PDF | Haute | Moyenne | Élevée |
| Collaboration entre étudiants (partage de quiz) | Moyenne | Haute | Moyenne |
| Internationalisation (EN/FR/AR) | Moyenne | Haute | Faible |
| Notifications push / email résultats | Faible | Moyenne | Faible |
| Application mobile (PWA) | Haute | Très haute | Post-v3.0.0 |
| Marketplace de cours partagés | Haute | Très haute | Long terme |

---

## Dépendances critiques

```
US-51 (Chiffrement clés)  ──────► US-70 (Déploiement prod)
US-50 (Rate Limiting)     ──────► US-70 (Déploiement prod)
US-40..44 (Pages légales) ──────► US-70 (Déploiement prod)
US-70 (Déploiement)       ──────► US-71 (Monitoring)
US-70 (Déploiement)       ──────► US-72 (Sauvegardes)
US-60 (Tests frontend)    ──────► US-73 (Pipeline CD, qualité requise)
```

> **Règle** : Aucun déploiement en production sans que US-50, US-51 et les pages légales soient terminées.

---

## Indicateurs de suivi (KPIs)

| KPI | Cible | Fréquence de mesure |
|-----|-------|---------------------|
| Vélocité de l'équipe | 30 SP / sprint | Fin de chaque sprint |
| Couverture de tests (frontend) | ≥ 70 % | Sprint 1, puis en continu |
| Nombre d'issues bloquantes (P0) | 0 en fin de sprint | Hebdomadaire |
| Taux de succès CI | ≥ 95 % | Hebdomadaire |
| Uptime production | ≥ 99 % | Après Sprint 4 |
| Score WCAG AA | 0 erreur sur 5 pages | Sprint 3 |
