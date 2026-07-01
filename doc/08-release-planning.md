# Release Planning — EduTutor IA

Équipe 16 · APOCAL'IPSSI 2026 · Semaine immersive Scrum

## Identification

| Champ            | Valeur                                                                                                                                     |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Équipe n°      | 16                                                                                                                                         |
| Membres          | Rania ZERAMDINI, Amani LAYOUNI, Badreddine CHEBBOUR, Taise de These NGANGA YABIE, Noah MASSET, Awadi BEDJA MROINKODO SAID, Clement BASTIEN |
| Sprint concerné | Cadrage                                                                                                                                    |
| Version          | v1.1 — intègre perturbation J1                                                                                                           |
| Date de remise   | 30/06/2026 13h00                                                                                                                           |
| Statut           | En revue PO                                                                                                                                |

---

## Vue d'ensemble

7 sprints d'une demi-journée chacun, du lundi 30 juin au jeudi 3 juillet 2026.
Équipe de 7 personnes · Capacité totale : 203 h-pers · Scope engagé : 56 SP (MUST 25 + SHOULD 31)

Deux releases attendues :

- Release 1 (MVP) : mercredi 2 juillet à 17h45 — parcours F1–F6 complet et stable
- Release 2 : jeudi 3 juillet à 17h00 — 2 à 3 fonctionnalités choisies avec le PO

---

## Planning des sprints

| Sprint          | Date        | Horaires       | Capacité (h-pers) | Vélocité cible (SP) | Objectif                                                                                                                   | Stories          | Jalon                                 |
| --------------- | ----------- | -------------- | ------------------ | --------------------- | -------------------------------------------------------------------------------------------------------------------------- | ---------------- | ------------------------------------- |
| Cadrage         | Lun 30 juin | 9h00–13h30    | 24,5               | n.c.                  | Produire les 7 artefacts agiles                                                                                            | n.c.             | Validation PO 14h00                   |
| Sprint 1        | Lun 30 juin | 14h00–18h00   | 28                 | 8                     | Fiabiliser F1 (auth) et F2 (upload) — cas limites, gestion d'erreurs, tests                                               | US-01, US-02     | Sprint Review 18h00                   |
| Sprint 2        | Mar 1 juil  | 9h00–12h30    | 24,5               | 8                     | Fiabiliser F3 (génération LLM < 60 s) + ADR fournisseur suite à perturbation J2                                         | US-03 + ADR-01   | Perturbation J2 à 10h00              |
| Sprint 3        | Mar 1 juil  | 14h00–18h00   | 28                 | 8                     | Fiabiliser F4 (soumission) et F5 (score) + intégrer le fournisseur retenu dans l'ADR                                      | US-04, US-05     | Sprint Review 18h00                   |
| Sprint 4        | Mer 2 juil  | 9h00–12h30    | 24,5               | 8                     | Finaliser F6 (historique) + patch sécurité suite à perturbation J3 (prompt injection + rate limiting) — US-21 si dispo | US-06 + patch J3 | Perturbation J3 à 10h00              |
| Sprint 5        | Mer 2 juil  | 14h00–18h00   | 28                 | 8                     | Export RGPD (US-12) suite à J3-bis + derniers correctifs F1–F6 — Release 1 livrée                                      | US-12            | J3-bis à 14h00 · Release 1 à 17h45 |
| Sprint 6        | Jeu 3 juil  | 9h00–12h30    | 24,5               | 8                     | Reset mdp (US-07) + suivi classe J1 (US-22) + investigation J4 — US-08/US-11 si capacité restante                        | US-07, US-22     | Perturbation J4 à 10h00              |
| Sprint 7        | Jeu 3 juil  | 14h00–17h00   | 21                 | 8                     | Timer (US-10) + niveau difficulté (US-09) + post-mortem J4 + répétition démo — US-08 ou US-11 si dispo                | US-09, US-10     | Release 2 à 17h00                    |
| Soutenance      | Ven 4 juil  | Selon planning | n.c.               | n.c.                  | Pitch 15 min + démo live R1 + R2 + retour réflexif sur les 5 perturbations                                               | n.c.             | Soutenance + jury                     |
| **Total** |             |                | **203**      | **56 SP**       |                                                                                                                            |                  |                                       |

---

## Les 5 perturbations

| Perturbation      | Date et heure         | Sujet                                                                                               | Impact planning                                                            | Story concernée                   |
| ----------------- | --------------------- | --------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- | ---------------------------------- |
| J1 — Produit     | Lun 29 juin, cadrage | Nouvelle persona enseignante (Mme Lefèvre)                                                         | 3 stories ajoutées au backlog, artefacts de cadrage à compléter         | US-21, US-22, US-23                |
| J2 — LLM         | Mar 30 juin, 10h00    | Latence inacceptable d'Ollama en CPU — choisir un fournisseur LLM alternatif, ADR obligatoire      | Rédiger ADR-01, possibilité de basculer sur Groq ou OpenAI               | US-03 + ADR-01                     |
| J3 — Sécurité  | Mer 1 juil, 10h00     | Faille détectée : prompt injection sur /api/llm/generate-quiz/                                    | Patch urgent en Sprint 4 : validation inputs + rate limiting 5 req/min     | patch J3 (sous-tâche US-03/US-04) |
| J3-bis — RGPD    | Mer 1 juil, 14h00     | Conformité RGPD obligatoire : 4 pages légales vides + droit d'accès SAR Art. 15 non implémenté | Pages légales + export données à livrer avant Release 1                 | US-12 (avancé en Sprint 5)        |
| J4 — Utilisateur | Jeu 3 juil, 10h00     | Signalements de questions LLM hors sujet ou hallucinées par des bêta-testeurs                     | Investigation + boucle de signalement à ajouter en Release 2 si capacité | US-16 (COULD)                      |

---

## Release 1 — MVP (mercredi 2 juillet, 17h45)

Stories livrées : US-01 (F1 auth) · US-02 (F2 upload) · US-03 (F3 génération) · US-04 (F4 passage) · US-05 (F5 score) · US-06 (F6 historique) · US-12 (export RGPD) · patch J3 (sécurité)

Pour considérer la Release 1 comme livrée :

- F1 : inscription, connexion, reset, profil fonctionnels et testés
- F2 : upload PDF <= 5 Mo et saisie texte >= 200 caractères, erreurs gérées proprement
- F3 : 10 QCM générés en < 60 s, fournisseur LLM documenté dans ADR-01
- F4 : soumission des réponses et correction automatique
- F5 : score /10 et détail des réponses affiché
- F6 : historique des quiz trié par date, accessible sur /history
- Patch J3 intégré : rate limiting actif, prompt injection bloquée
- Pages légales J3-bis publiées : au moins mentions légales et politique de confidentialité
- Tag Git v1.0.0 créé sur main, CI verte
- Démo live jouable sur localhost:3000

---

## Release 2 — Fonctionnalités enrichies (jeudi 3 juillet, 17h00)

Choisir 2 à 3 stories parmi les candidates ci-dessous avec le PO avant le Sprint 6.

| US    | Titre                                       | SP | Perturbation | Recommandation                                                   |
| ----- | ------------------------------------------- | -- | ------------ | ---------------------------------------------------------------- |
| US-07 | Réinitialiser le mot de passe              | 3  | —           | Rapide à livrer (lien magique 1h), attendu par les testeurs     |
| US-08 | Bibliothèque de cours uploadés            | 5  | —           | Débloque les tests de régression sur F2                        |
| US-09 | Niveau de difficulté + nb questions        | 5  | —           | Impact fort sur la qualité des quiz en démo                    |
| US-10 | Mode timer optionnel                        | 3  | —           | Effet démo visible, développement rapide                       |
| US-11 | Dashboard de progression                    | 5  | —           | Répond directement à la promesse produit pour Léa Martin      |
| US-22 | Suivi progression étudiants (Mme Lefèvre) | 5  | J1           | Répond à la perturbation J1, valeur démo élevée             |
| US-16 | Identifier lacunes (si capacité + J4)      | 8  | J4           | Lié au signalement J4, ambitieux — à évaluer après Sprint 6 |

Pour considérer la Release 2 comme livrée :

- Au moins 2 stories SHOULD terminées et démontrables
- Post-mortem J4 rédigé (1 page : impact, décision prise, leçon retenue)
- Tag Git v2.0.0 créé sur main, CI verte
- Démo R1 + R2 répétée et prête pour vendredi

---

## Burnup global

Scope initial : 56 SP (MUST 25 + SHOULD 31, après intégration J1). À mettre à jour après chaque Sprint Review.

| Sprint   | Fin de sprint      | SP livrés (idéal) | SP livrés (réel) | Scope total |
| -------- | ------------------ | ------------------- | ------------------ | ----------- |
| Cadrage  | Lun 29 juin 13h00 | 0                   |                    | 56 SP       |
| Sprint 1 | Lun 30 juin 17h00  | 8                   |                    | 56 SP       |
| Sprint 2 | Mar 30 juin 12h30 | 16                  |                    | 56 SP       |
| Sprint 3 | Mar 1 juil 17h00   | 24                  |                    | 56 SP       |
| Sprint 4 | Mer 2 juil 12h30   | 32                  |                    | 56 SP       |
| Sprint 5 | Mer 2 juil 18h00   | 40                  |                    | 56 SP       |
| Sprint 6 | Jeu 3 juil 12h30   | 48                  |                    | 56 SP       |
| Sprint 7 | Jeu 3 juil 17h00   | 56                  |                    | 56 SP       |

Si l'écart entre le réel et l'idéal dépasse 8 SP à la fin d'un sprint, revoir le scope avec le PO immédiatement plutôt qu'en fin de semaine.

---

## ADR à produire pendant la semaine

| ADR    | Sujet                                                               | Déclencheur    | À rédiger              |
| ------ | ------------------------------------------------------------------- | --------------- | ------------------------ |
| ADR-01 | Choix du fournisseur LLM (Ollama local, Groq, OpenAI, autre)        | Perturbation J2 | Sprint 2, mardi matin    |
| ADR-02 | Stratégie de rate limiting (django-ratelimit ou middleware custom) | Perturbation J3 | Sprint 4, mercredi matin |

---

## Dépendances entre sprints

Release 1 bloque Release 2 : ne pas démarrer les stories R2 avant que F1–F6 soient en Done.

ADR-01 (J2) → US-03 : le choix du fournisseur LLM conditionne la finalisation de la génération de quiz (EP-03 — F3).

US-02 → US-03 → US-04 → US-05 → US-06 : le parcours quiz est séquentiel, chaque étape dépend de la précédente (upload → génération → soumission → score → historique).

US-12 (export RGPD) → Release 1 : aucune mise en production sans conformité légale minimale (déclenché par J3-bis).

---

## Auto-évaluation

| Critère                                                   | Statut | Remarque |
| ---------------------------------------------------------- | ------ | -------- |
| 7 sprints planifiés avec date, horaires et capacité      |        |          |
| Chaque sprint a un objectif mesurable et livrable en démo |        |          |
| Chaque sprint liste au moins une story engagée            |        |          |
| Release 1 positionnée en fin de Sprint 5 (mercredi 17h45) |        |          |
| Release 2 positionnée en fin de Sprint 7 (jeudi 17h00)    |        |          |
| Les 5 perturbations sont positionnées aux bons créneaux  |        |          |
| Perturbation J1 intégrée avec impact sur le backlog      |        |          |
| Burnup initialisé avec scope chiffré                     |        |          |
| Planning co-construit en équipe                           |        |          |
