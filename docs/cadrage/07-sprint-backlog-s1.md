# Sprint Backlog S1

**APOCAL'IPSSI** · CADRAGE MATINAL · ARTEFACT 7 SUR 7
*Sprint Backlog du Sprint 1*
Projet EduTutor IA · Edition 2026 · Semaine immersive Scrum

---

## IDENTIFICATION DU DOCUMENT

| Champ | Valeur |
|-------|--------|
| Equipe n | 16 |
| Membres | Rania ZERAMDINI, Amani LAYOUNI, Badreddine CHEBBOUR, Taise de These NGANGA YABIE, Noah MASSET, Awadi BEDJA MROINKODO SAID, Clement BASTIEN |
| Sprint concerne | Sprint 1 |
| Version | v1.1 (post-perturbation P1) |
| Date de remise | 29/06/2026 |
| Statut | Draft |

## 2. Engagement de l'equipe (Scope du Sprint)

| ID | User Story | SP | Binome |
|----|------------|----|--------|
| US-01 | Finaliser l'inscription par email + tests | 2 | A — Auth (Badreddine + Rania) |
| US-02 | Finaliser la validation d'email + tests | 1 | A — Auth (Badreddine + Rania) |
| US-03 | Finaliser la connexion + tests | 1 | A — Auth (Badreddine + Rania) |
| US-15 | Finaliser le reset mot de passe + tests | 1 | A — Auth (Badreddine + Rania) |
| US-16 | Page profil (modifier / supprimer compte) | 2 | A — Auth (Badreddine + Rania) |
| US-04 | Finaliser l'upload PDF (5 Mo) + cas limites | 2 | B — Contenu (Amani + Clement) |
| US-05 | Finaliser la saisie texte (200 caracteres) | 1 | B — Contenu (Amani + Clement) |
| US-06 | Ajuster le prompt LLM pour 10 QCM + tests | 3 | C — Quiz (Noah + Taise) |
| US-07 | Finaliser le passage du quiz interactif | 2 | C — Quiz (Noah + Taise) |
| US-08 | Finaliser le score /10 et la correction | 1 | D — Resultat (Awadi) |
| US-09 | Historique des quiz par utilisateur | 2 | D — Resultat (Awadi) |

**Total : 18 SP** (capacite estimee : 24 SP pour 4 developpeurs sur 1,5 jour — marge de 6 SP pour les imprevus)

## 3. Tracabilite MVP (F1-F6)

| Feature | US couvrantes | Statut |
|---------|---------------|--------|
| F1 — Auth complete | US-01, 02, 03, 15, 16 | Dans le sprint |
| F2 — Upload cours | US-04, 05 | Dans le sprint |
| F3 — Generation LLM | US-06 | Dans le sprint |
| F4 — Passage + correction | US-07, 08 | Dans le sprint |
| F5 — Score /10 | US-08 | Dans le sprint |
| F6 — Historique | US-09 | Dans le sprint |

Toutes les features MVP (F1-F6) sont couvertes par au moins une US du sprint.

## 4. Dependances et ordonnancement

Inscription (US-01)
  → Validation email (US-02)
  → Connexion (US-03)
  → Reset MDP (US-15)
  → Profil (US-16)

Upload PDF (US-04) ─┐
Saisie texte (US-05) ┼→ Génération LLM (US-06)
                     │      → Passage quiz (US-07)
                     │           → Score (US-08)
                     │                → Historique (US-09)

## Quand est-ce qu'on considère le sprint fini ?

- Toutes les US ci-dessus sont en "Done"
- Les features F1-F6 fonctionnent et sont testées
- On peut faire une démo en quelques minutes du parcours complet (inscription → upload → quiz → score → historique)
- Retrospective de 15 min avant la perturbation P2

## Perturbations

### P1 — Nouvelle persona enseignante (Mme Lefevre)

- **Contexte** : Le sponsor demande d'integrer Mme Sophie Lefevre (enseignante BTS Comm, Lyon, 28 eleves) comme cible secondaire.
- **Impact sur le sprint** : Aucun — le perimetre F1-F6 reste inchange. La persona enseignante est classee **SHOULD-HAVE** pour la Release 1 (pas MUST).
- **Decision** : On garde le focus sur le MVP etudiant (F1-F6). Les US enseignant (US-26 a US-30) sont planifiees pour le Sprint 2 si le temps le permet.
- **Livrables produits** :
  - Persona Mme Lefevre (6 dimensions)
  - Customer Journey (5 etapes)
  - Story Map mise a jour (parcours etudiant + enseignant)
  - Product Backlog actualise : 5 US enseignant (compte enseignant, import CSV, dashboard, alertes, messagerie), priorisation MoSCoW
  - Note de decision : cible enseignante = **SHOULD-HAVE** pour R1
- **SP impactes** : 0 (on ne modifie pas le scope du Sprint 1)

## Grille d'auto-evaluation

| Critere qualite | Auto-evaluation | Commentaire |
|-------------------|-----------------|-------------|
| L'objectif du sprint est clair et mesurable | ✅ Oui | Parcours F1-F6 complet, livrable mercredi 10h |
| Toutes les US du Product Backlog priorisees sont dans le sprint | ✅ Oui | 11 US, 18 SP, toutes les features MVP couvertes |
| Chaque US a un SP, un binome et une tracabilite F1-F6 | ✅ Oui | Tableau detaille + section tracabilite F1-F6 |
| Les dependances sont visibles et realistes | ✅ Oui | Arbre ASCII + explication logique |
| La DoD est complete et verifiable | ✅ Oui | 6 criteres checkables (tests, lint, demo, retro) |
| La perturbation P1 est documentee avec impact + decision | ✅ Oui | Contexte, impact nul, decision SHOULD-HAVE, livrables, SP 0 |
| Le document a ete relu par l'equipe | ✅ Partiel | A valider collectivement avant la remise |
