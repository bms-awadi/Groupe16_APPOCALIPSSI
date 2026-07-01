# 📐 Cadrage matinal — EduTutor IA

Le **cadrage matinal** est le rituel qui ouvre la semaine immersive
APOCAL'IPSSI 2026 : lundi 9h00–13h30, avant que la première ligne de code ne
soit écrite (le Sprint 1 démarre à 14h00). L'équipe y transforme le brief
produit **EduTutor IA** en un backlog priorisé et un planning de sprint,
en suivant une démarche agile classique (Pichler, Scrum).

## 🎯 Pourquoi ce rituel

Sans cadrage, une équipe code des features au fil de l'eau sans vision
partagée — premier symptôme d'un projet qui dérive. Le cadrage matinal force
l'équipe à répondre, **avant de coder**, à des questions structurantes :

- Qui sont nos utilisateurs réels, et avec quels besoins chiffrés ?
- À quel moment précis du parcours utilisateur décroche-t-on, et pourquoi ?
- Quel est le périmètre du MVP, et qu'est-ce qu'on assume explicitement de
  ne **pas** faire (MoSCoW) ?
- Comment ce périmètre se découpe-t-il en 7 sprints d'une demi-journée ?
- Quelles sont les toutes premières tâches techniques du Sprint 1 ?

Chaque artefact du dossier répond à une de ces questions, et s'appuie sur le
précédent (Vision → Personas → Parcours → Story Map → Planning → Backlog →
Sprint Backlog). Ne pas sauter d'étape : un Product Backlog rédigé sans
Story Map en amont produit des priorités arbitraires.

## 🛠️ Méthode de travail attendue

- **Travailler en binôme minimum**, jamais en solo — les artefacts de
  cadrage (personas, vision) sont sujets à biais de projection individuel.
- Pour les artefacts visuels (Customer Journey, Story Map), **étaler les
  données sur un grand format** (post-it, tableau blanc) avant de les
  reporter dans le document — le travail collaboratif en amont produit de
  meilleurs résultats qu'un remplissage solo à l'écran.
- **Recommitter à chaque révision majeure** (suite à une perturbation) avec
  un nouveau numéro de version et un message Git explicite.
- Faire valider chaque livrable par le **Product Owner** avant de le
  considérer comme acquis (statut `Validé PO`, avec trace écrite).
- Avant soumission, **remplir la grille d'auto-évaluation** présente en fin
  de chaque document — un livrable avec plusieurs lignes en « Partiel »
  signale un besoin de revue collective.

## 🔄 Cycle de vie d'un document

`Draft` → `En revue PO` → `Validé PO` → `Archivé`, avec versionnement
`v1.0` (cadrage initial) → `v1.1`/`v1.2` (révisions mineures post-revue) →
`v2.0` (révision majeure post-perturbation).

## 📋 Pour la liste concrète des tâches

👉 Voir [A-FAIRE.md](./A-FAIRE.md) pour le détail artefact par artefact :
ce qui est imposé (MVP F1-F6, cibles, perturbations), ce qu'il reste à
compléter dans chaque PDF, la convention de nommage, et où ces documents
s'intègrent dans le reste du repo.
