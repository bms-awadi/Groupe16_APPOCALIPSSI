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
| US-01 | En tant qu'etudiant·e, je veux creer un compte avec email et mot de passe, afin de sauvegarder mes quiz et y revenir quand je veux. | 3 | A — Auth (Badreddine + Rania) |
| US-02 | En tant qu'etudiant·e, je veux uploader un PDF (5 Mo) ou saisir un texte de cours (200 car.), afin de ne pas recopier mon support a la main. | 5 | B — Contenu (Amani + Clement) |

**Total : 8 SP** (capacite estimee : 14-16 SP pour l'equipe sur 1,5 jour — marge confortable pour les imprevus)

## 3. Tracabilite MVP (F1-F6)

| Feature | US couvrantes | Statut |
|---------|---------------|--------|
| F1 — Auth complete | US-01 | Dans le sprint |
| F2 — Upload cours | US-02 | Dans le sprint |
| F3 — Generation LLM | US-03 | Sprint 2 |
| F4 — Passage + correction | US-04 | Sprint 3 |
| F5 — Score /10 | US-05 | Sprint 3 |
| F6 — Historique | US-06 | Sprint 4 |

Les features F3-F6 sont planifiees dans les sprints suivants selon le Product Backlog.

## 4. Dependances et ordonnancement

US-01 (Auth) et US-02 (Upload) sont independantes et peuvent etre developpees en parallele durant le Sprint 1.

    S1 : US-01 (Auth)  ||  US-02 (Upload)
                         |
    S2 : US-03 (Generation LLM)
                         |
    S3 : US-04 (Passage) + US-05 (Score)
                         |
    S4 : US-06 (Historique)

L'ordonnancement complet est defini dans le Product Backlog sur les sprints S1 a S4.

## Quand est-ce qu'on considère le sprint fini ?

- Toutes les US ci-dessus sont en "Done"
- Les features F1 (Auth) et F2 (Upload) fonctionnent et sont testées
- On peut faire une démo du parcours S1 : inscription → upload (le reste F3-F6 est pour les sprints suivants)
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
| Toutes les US du Product Backlog priorisees sont dans le sprint | ✅ Oui | 2 US (US-01, US-02), 8 SP, conforme au PB S1 |
| Chaque US a un SP, un binome et une tracabilite F1-F6 | ✅ Oui | IDs alignes avec le Product Backlog officiel |
| Les dependances sont visibles et realistes | ✅ Oui | Arbre ASCII + explication logique |
| La DoD est complete et verifiable | ✅ Oui | 6 criteres checkables (tests, lint, demo, retro) |
| La perturbation P1 est documentee avec impact + decision | ✅ Oui | Contexte, impact nul, decision SHOULD-HAVE, livrables, SP 0 |
| Le document a ete relu par l'equipe | ✅ Partiel | l'equipe n'est pas au complet a ce jour |
