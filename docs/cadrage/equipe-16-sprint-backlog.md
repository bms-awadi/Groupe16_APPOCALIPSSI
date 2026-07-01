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


## Sprint 2

### 2. Engagement de l'equipe (Scope du Sprint)

| ID | User Story | SP | Binome |
|----|------------|----|--------|
| US-03 | En tant qu'etudiant·e, je veux generer un quiz de 10 QCM en moins de 60 s a partir de mon cours, afin de reviser rapidement un chapitre. | 8 | C — Quiz (Noah + Taise) |

**Total : 8 SP** (capacite estimee : 14-16 SP pour l'equipe sur 1,5 jour)

Les membres restants (Badreddine, Rania, Amani, Clement, Awadi) assurent le support qualite sur F1-F2 (tests de non-regression, correction de bugs) et la preparation technique pour S3.

### 3. Tracabilite MVP (F1-F6)

| Feature | US couvrantes | Statut |
|---------|---------------|--------|
| F1 — Auth complete | US-01 | Done (S1) |
| F2 — Upload cours | US-02 | Done (S1) |
| F3 — Generation LLM | US-03 | Dans le sprint |
| F4 — Passage + correction | US-04 | Sprint 3 |
| F5 — Score /10 | US-05 | Sprint 3 |
| F6 — Historique | US-06 | Sprint 4 |

F1 et F2 sont livrees et testees. F3 est le focus du Sprint 2.

### 4. Dependances et ordonnancement

US-03 (Generation LLM) depend de US-02 (Upload) : il faut un cours uploade pour generer un quiz.

    S1 : US-01 (Auth)  ||  US-02 (Upload)  [DONE]
                         |
    S2 : US-03 (Generation LLM)  [EN COURS]
                         |
    S3 : US-04 (Passage) + US-05 (Score)
                         |
    S4 : US-06 (Historique)

### Quand est-ce qu'on considère le sprint fini ?

- US-03 est en "Done" (genere 10 QCM en < 60 s sur gpu, tests OK)
- La feature F3 (Generation LLM) fonctionne et est testee
- On peut faire une demo du parcours S1-S2 : inscription → upload → generation de quiz
- F1 et F2 restent stables (pas de regression)
- Retrospective de 15 min

### Perturbations

Aucune perturbation declaree pour le Sprint 2. Le focus reste sur le MVP etudiant F1-F6.

### Grille d'auto-evaluation Sprint 2

| Critere qualite | Auto-evaluation | Commentaire |
|-------------------|-----------------|-------------|
| L'objectif du sprint est clair et mesurable | ✅ Oui | Generation de 10 QCM en < 60 s (F3, sur gpu), livrable mardi soir |
| Toutes les US du Product Backlog priorisees sont dans le sprint | ✅ Oui | 1 US (US-03), 8 SP, conforme au PB S2 |
| Chaque US a un SP, un binome et une tracabilite F1-F6 | ✅ Oui | IDs alignes avec le Product Backlog officiel |
| Les dependances sont visibles et realistes | ✅ Oui | Arbre ASCII + dependance US-03 → US-02 |
| La DoD est complete et verifiable | ✅ Oui | 5 criteres checkables (gen < 60 s, tests, demo S1-S2, pas de regression, retro) |
| Le document a ete relu par l'equipe | ✅ Partiel | l'equipe n'est pas au complet a ce jour |

---

## Sprint 3

### 2. Engagement de l'equipe (Scope du Sprint)

| ID | User Story | SP | Binome |
|----|------------|----|--------|
| US-04 | En tant qu'etudiant·e, je veux soumettre mes reponses et obtenir la correction, afin de verifier mes connaissances. | 5 | D — Passage (Amani + Awadi) |
| US-05 | En tant qu'etudiant·e, je veux voir mon score /10 et le detail des reponses, afin de connaitre mes points forts et mes lacunes. | 3 | E — Score (Clement + Rania) |

**Total : 8 SP** (capacite estimee : 14-16 SP pour l'equipe sur 1 jour — marge pour perturbations et stabilisation MVP)

Les membres restants (Badreddine, Noah, Taise) assurent le support qualite sur F1-F3, le patch securite J3, et les livrables RGPD J3-bis.

### 3. Tracabilite MVP (F1-F6)

| Feature | US couvrantes | Statut |
|---------|---------------|--------|
| F1 — Auth complete | US-01 | Done (S1) |
| F2 — Upload cours | US-02 | Done (S1) |
| F3 — Generation LLM | US-03 | Done (S2) |
| F4 — Passage + correction | US-04 | Dans le sprint |
| F5 — Score /10 | US-05 | Dans le sprint |
| F6 — Historique | US-06 | Sprint 4 |

F1, F2 et F3 sont livrees et testees. F4 et F5 sont le focus du Sprint 3.

### 4. Dependances et ordonnancement

US-04 (Passage) et US-05 (Score) dependent de US-03 (Generation) : il faut un quiz genere pour pouvoir y repondre et obtenir un score.

    S1 : US-01 (Auth)  ||  US-02 (Upload)  [DONE]
                         |
    S2 : US-03 (Generation LLM)  [DONE]
                         |
    S3 : US-04 (Passage) + US-05 (Score)  [EN COURS]
                         |
    S4 : US-06 (Historique)

### Quand est-ce qu'on considere le sprint fini ?

- US-04 et US-05 sont en "Done" (passage fonctionnel, score calcule cote serveur, affichage detaille)
- Les features F4 (Passage) et F5 (Score) fonctionnent et sont testees
- On peut faire une demo du parcours S1-S3 : inscription → upload → generation → passage → score
- F1, F2 et F3 restent stables (pas de regression)
- Patch J3 (securite) integre et teste
- Livrables J3-bis (RGPD) produits et pousses sur GitHub
- Tag Git v1.0.0 cree sur main pour la Release 1 (MVP)
- Retrospective de 15 min

### Perturbations

#### P3 — Securite (prompt injection)

- **Contexte** : Une faille de prompt injection est detectee sur `/api/llm/generate-quiz/`. Un utilisateur malveillant peut injecter des instructions dans le texte du cours pour manipuler la sortie du LLM.
- **Impact sur le sprint** : Patch urgent a livrer avant la Release 1. Ralentissement temporaire du developpement F4-F5 pour 2 membres.
- **Decision** : Badreddine et Noah prennent en charge le patch securite (validation inputs + rate limiting 5 req/min). Le reste de l'equipe continue F4-F5.
- **Livrables produits** :
  - Patch validation inputs cote backend
  - Rate limiting 5 req/min sur `/api/llm/generate-quiz/`
  - Tests de non-regression sur la generation de quiz
- **SP impactes** : 0 (le patch est traite en parallele, hors scope sprint)

#### P3-bis — RGPD / Donnees personnelles (J3-bis)

- **Contexte** : Hugo Petit, utilisateur de la plateforme, formule une demande d'acces aux donnees personnelles au titre de l'article 15 du RGPD. La plateforme n'a pas encore d'export RGPD ni de pages legales completes.
- **Impact sur le sprint** : Demande de conformite urgente a traiter avant la Release 1. Le developpement complet est hors scope MVP (delai trop court).
- **Decision** : Posture de conformite documentee. L'equipe produit 5 livrables documentaires (pas de code) et planifie l'implementation post-MVP.
- **Livrables produits** :
  1. `docs/rgpd/endpoint-export-rest.md` — Specification de l'endpoint `GET /api/accounts/me/export/`
  2. `docs/rgpd/bouton-frontend-export.md` — Specification du bouton "Exporter mes donnees"
  3. `docs/rgpd/politique-retention.md` — Politique de retention (3 sections : durees, motifs legaux, suppression Art. 17)
  4. `docs/rgpd/audit-trail-sar.md` — Specification du modele `DataRequest` (audit trail SAR)
  5. `docs/rgpd/reponse-hugo-petit.md` — Reponse professionnelle a Hugo Petit
- **SP impactes** : 0 (livres documentaires, pas de developpement)

### Grille d'auto-evaluation Sprint 3

| Critere qualite | Auto-evaluation | Commentaire |
|-------------------|-----------------|-------------|
| L'objectif du sprint est clair et mesurable | ✅ Oui | F4 (Passage) + F5 (Score) + patch securite + livrables RGPD |
| Toutes les US du Product Backlog priorisees sont dans le sprint | ✅ Oui | 2 US (US-04, US-05), 8 SP |
| Chaque US a un SP, un binome et une tracabilite F1-F6 | ✅ Oui | IDs alignes avec le Product Backlog officiel |
| Les dependances sont visibles et realistes | ✅ Oui | Arbre ASCII + dependance US-04/05 → US-03 |
| La DoD est complete et verifiable | ✅ Oui | 7 criteres checkables (tests, demo S1-S3, patch J3, RGPD, tag v1.0.0, retro) |
| Les perturbations P3 et P3-bis sont documentees avec impact + decision | ✅ Oui | Contexte, impact, decision, livrables, SP 0 |
| Le document a ete relu par l'equipe | ✅ Oui | Relu en fin de journee avant livraison MVP |

## Sprint 4

*A completer jeudi*
