# Contexte & Vision du Projet — EduTutor IA

## 1. Contexte du projet

**Nom du projet** : EduTutor IA  
**Code interne** : APPOCALIPSSI – Groupe 16  
**Établissement** : IPSSI  
**Type** : Reprise d'un projet existant partiellement développé  
**Date de reprise** : Juin 2026  
**Statut initial** : MVP1 + MVP2 livrés, plusieurs lacunes identifiées à combler

---

### 1.1 Description générale

EduTutor IA est une **plateforme de révision personnalisée** qui exploite des modèles de langage (LLM) pour générer automatiquement des quiz à partir de documents de cours fournis par les étudiants. Le système prend en charge les PDF (≤ 5 Mo) et les textes libres (≥ 200 caractères), génère 10 questions à choix multiples, note les réponses et conserve un historique de progression.

### 1.2 État du projet à la reprise

| Composant | État |
|-----------|------|
| Authentification email (signup, login, reset) | Terminé |
| Génération de quiz via LLM (9 fournisseurs) | Terminé |
| Prise de quiz & notation | Terminé |
| Interface d'administration | Terminé |
| Dashboard de progression | Partiellement terminé (MVP2 démo) |
| Revue des erreurs | Partiellement terminé (MVP2 démo) |
| Pages légales (CGU, mentions, confidentialité, cookies) | Placeholder vide |
| Tests unitaires frontend | Quasi inexistants (1 fichier) |
| Rate limiting des endpoints | Absent |
| Chiffrement des clés API | Absent |
| Logs structurés | Absent |
| Recherche dans l'historique | Absent |
| Déploiement production | Non effectué |
| Audit accessibilité WCAG | Non effectué |

---

## 2. Énoncé de vision

> **Pour** les étudiants cherchant à réviser efficacement,  
> **qui** n'ont pas accès à des exercices personnalisés sur leurs cours spécifiques,  
> **EduTutor IA** est une plateforme web de révision automatisée,  
> **qui** génère des quiz interactifs à partir de leurs propres documents de cours,  
> **contrairement** aux plateformes génériques (Quizlet, Kahoot),  
> **notre solution** s'adapte exactement au contenu fourni par l'étudiant grâce à l'intelligence artificielle, sans nécessiter de création manuelle de questions.

---

## 3. Objectifs SMART

| # | Objectif | Spécifique | Mesurable | Réalisable | Pertinent | Temporel |
|---|----------|-----------|-----------|-----------|----------|----------|
| O1 | Stabiliser la qualité du code | Couvrir les pages frontend par des tests unitaires | Couverture ≥ 70 % sur les composants critiques | Oui (vitest déjà configuré) | Oui (CI déjà en place) | Sprint 1 |
| O2 | Mise en conformité légale | Rédiger les 4 pages légales (CGU, mentions, confidentialité, cookies) | 4 pages publiées et validées | Oui (templates fournis) | Obligatoire RGPD | Sprint 2 |
| O3 | Sécuriser l'application | Implémenter le rate limiting et chiffrer les clés API | 0 endpoint sans rate limit, 0 clé en clair | Oui | Oui (risque sécurité identifié) | Sprint 2 |
| O4 | Améliorer l'expérience utilisateur | Recherche dans l'historique, accessibilité WCAG AA | Filtre fonctionnel + score WCAG AA | Oui | Oui | Sprint 3 |
| O5 | Déployer en production | Déploiement sur VPS OVH avec Caddy + HTTPS | URL publique accessible, uptime ≥ 99 % | Oui (guide existant) | Oui | Sprint 4 |

---

## 4. Périmètre du projet

### Dans le périmètre (In Scope)

- Maintenance et amélioration du backend Django existant
- Maintenance et amélioration du frontend React/TypeScript existant
- Rédaction du contenu des pages légales
- Mise en place du rate limiting
- Chiffrement des clés API LLM en base de données
- Mise en place de logs structurés et d'un audit trail
- Implémentation de la recherche/filtrage dans l'historique des quiz
- Tests unitaires et d'intégration complémentaires
- Audit et corrections d'accessibilité WCAG AA
- Déploiement en production sur VPS OVH
- Mise en place d'un système de monitoring

### Hors périmètre (Out of Scope)

- Refonte complète de l'architecture
- Changement de stack technologique
- Application mobile native
- Module de collaboration entre étudiants
- Marketplace de cours

---

## 5. Contraintes

| Type | Contrainte |
|------|-----------|
| **Technologique** | Stack imposée : Django 5.1, React 18, PostgreSQL 16, Docker |
| **Financière** | Budget infrastructure limité (VPS OVH entrée de gamme) |
| **Réglementaire** | Conformité RGPD obligatoire (pages légales, gestion des données) |
| **Temporelle** | Projet découpé en 4 sprints de 2 semaines |
| **Humaine** | Équipe de 4 à 5 développeurs étudiants |
| **Qualité** | CI/CD existant (GitHub Actions) — aucun merge sans tests verts |

---

## 6. Critères de succès

1. Toutes les pages légales sont rédigées et publiées
2. Aucune clé API n'est stockée en clair en base de données
3. Tous les endpoints critiques sont protégés par un rate limit
4. La couverture de tests frontend atteint ≥ 70 % sur les composants critiques
5. L'application est accessible en production via HTTPS
6. Le score WCAG AA est atteint sur les pages principales
7. Un système de monitoring envoie des alertes en cas de panne

---

## 7. Liens utiles

| Ressource | Lien |
|----------|------|
| Documentation technique | `docs/` (répertoire racine) |
| Guide démarrage | `GUIDE-ETUDIANT.md` |
| Guide contribution | `CONTRIBUTING.md` |
| Historique des versions | `CHANGELOG.md` |
| Documentation architecture | `docs/01-architecture.md` |
| Guide déploiement VPS | `docs/11-deploiement-vps-ovh.md` |
