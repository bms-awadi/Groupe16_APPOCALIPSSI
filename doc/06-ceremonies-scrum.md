# Cérémonies Scrum — EduTutor IA

Templates et guides pour les 5 cérémonies Scrum de l'équipe Groupe 16.

---

## 1. Sprint Planning

**Durée** : 2 à 4 heures (max 4h pour un sprint de 2 semaines)  
**Participants** : PO, Scrum Master, toute l'équipe de développement  
**Fréquence** : Début de chaque sprint

### Ordre du jour

1. **Introduction** (15 min)
   - Le PO présente les US les mieux prioritées du backlog
   - Rappel de la vélocité passée et de la capacité disponible

2. **Sélection des US** (1h)
   - L'équipe choisit les US à intégrer au sprint
   - Chaque US est lue à voix haute, les critères d'acceptation sont vérifiés
   - Vérification de la DoR pour chaque US sélectionnée

3. **Planning Poker** (si nécessaire) (30 min)
   - Re-estimation des US non encore estimées ou dont la compréhension a changé
   - Cartes : 1, 2, 3, 5, 8, 13, 21, ∞ (trop grosse), ? (je ne sais pas)

4. **Décomposition en tâches** (1h30)
   - Pour chaque US sélectionnée, l'équipe identifie les tâches techniques
   - Chaque tâche est estimée en heures (idéalement < 1 jour)
   - Les tâches sont ajoutées au tableau Kanban du sprint

5. **Définition du Sprint Goal** (15 min)
   - Formuler le Sprint Goal en une phrase (voir template ci-dessous)
   - Vérifier que le Sprint Goal est atteignable avec les US sélectionnées

### Template Sprint Goal

> *"À la fin de ce sprint, [qui bénéficie] peut [faire quoi] grâce à [ce qu'on livre]."*

**Exemple** :
> "À la fin de ce sprint, l'équipe de développement peut merger en confiance grâce à une suite de tests unitaires couvrant les 5 pages frontend critiques."

### Checklist Sprint Planning

- [ ] Vélocité passée consultée et capacité calculée
- [ ] Toutes les US sélectionnées satisfont la DoR
- [ ] Les US sont décomposées en tâches < 1 jour
- [ ] Le Sprint Goal est rédigé et affiché
- [ ] Le tableau Kanban du sprint est rempli
- [ ] Chaque membre a des tâches assignées pour les 2 premiers jours

---

## 2. Daily Scrum (Mêlée Quotidienne)

**Durée** : 15 minutes maximum (timeboxé)  
**Participants** : Équipe de développement (PO et SM en observateurs si nécessaire)  
**Fréquence** : Chaque jour ouvré, à heure fixe  
**Format** : Debout, même endroit ou même channel (présentiel ou remote)

### Les 3 questions

Chaque membre répond **en moins de 2 minutes** :

1. **Qu'ai-je fait hier ?**  
   → Tâches terminées, PR soumises, blocages résolus

2. **Que vais-je faire aujourd'hui ?**  
   → Tâches prévues, objectif de la journée

3. **Ai-je des impediments ?**  
   → Blocages techniques, dépendances, questions sans réponse

> ⚠️ Le Daily Scrum n'est PAS une réunion de statut pour le management. C'est une synchronisation d'équipe. Les discussions techniques se font APRÈS la mêlée.

### Template Daily (asynchrone — Slack/Discord)

```
**Daily [Date] — [Prénom]**

✅ Hier :
- [tâche 1]
- [tâche 2]

🔜 Aujourd'hui :
- [tâche 1]
- [tâche 2]

🚧 Impediments :
- [bloqage ou AUCUN]
```

### Indicateurs à surveiller au Daily

- Burndown chart : la courbe descend-elle comme prévu ?
- Y a-t-il des tâches en "In Progress" depuis > 2 jours ? (risque de dérive)
- Des US risquent-elles de ne pas être terminées avant la fin du sprint ?

---

## 3. Sprint Review

**Durée** : 1 à 2 heures (max 2h pour un sprint de 2 semaines)  
**Participants** : PO, Scrum Master, équipe de développement, parties prenantes invitées  
**Fréquence** : Fin de chaque sprint

### Ordre du jour

1. **Introduction** (10 min)
   - Le Scrum Master rappelle le Sprint Goal et les US planifiées
   - Présentation du contexte (vélocité, incidents)

2. **Démonstration de l'incrément** (40 min)
   - Chaque US terminée est démontrée en direct (pas de slides, code en live)
   - Le PO valide ou invalide chaque US selon les critères d'acceptation
   - Les parties prenantes posent des questions

3. **Discussion backlog** (20 min)
   - Le PO présente les évolutions du backlog suite aux retours
   - Les nouvelles US émergentes sont discutées (pas estimées ici)

4. **Adaptation** (10 min)
   - Le PO annonce les priorités pour le prochain sprint

### Template compte-rendu Sprint Review

```markdown
# Sprint Review — Sprint [N]
**Date** : [date]  
**Sprint Goal** : [texte]

## US livrées (DoD validée)
| ID | Titre | SP |
|----|-------|----|
| US-XX | [titre] | X |

## US non livrées (retour au backlog)
| ID | Titre | Raison |
|----|-------|--------|
| US-XX | [titre] | [raison] |

## Vélocité réelle : X SP / X SP planifiés

## Retours des parties prenantes
- [retour 1]
- [retour 2]

## Décisions prises
- [décision 1]

## Prochain sprint — Top 3 priorités
1. [US ou thème]
2. [US ou thème]
3. [US ou thème]
```

---

## 4. Rétrospective Sprint

**Durée** : 1h30 (max 1h30 pour un sprint de 2 semaines)  
**Participants** : Scrum Master, équipe de développement (PO en option)  
**Fréquence** : Fin de chaque sprint, après la Sprint Review

### Format recommandé : "Étoile de mer"

```
                    ┌─────────────────┐
                    │  CONTINUER      │  → Ce qui fonctionne bien
                    │  (Keep doing)   │
                    └─────────────────┘
        ┌──────────────────┐    ┌──────────────────┐
        │  PLUS DE          │    │  MOINS DE         │
        │  (More of)        │    │  (Less of)        │
        └──────────────────┘    └──────────────────┘
        ┌──────────────────┐    ┌──────────────────┐
        │  COMMENCER        │    │  ARRÊTER          │
        │  (Start doing)    │    │  (Stop doing)     │
        └──────────────────┘    └──────────────────┘
```

### Déroulement

1. **Check-in** (5 min) : Niveau d'énergie de chaque membre (1 mot)
2. **Collecte des items** (20 min) : Chacun écrit sur des post-its (1 idée = 1 post-it)
3. **Regroupement** (10 min) : SM regroupe les items similaires
4. **Vote** (5 min) : Chacun vote pour les 3 items les plus importants
5. **Discussion** (30 min) : Focus sur les items les plus votés
6. **Actions** (15 min) : 1 à 3 actions concrètes avec responsable et date
7. **Check-out** (5 min) : Chacun dit comment il se sent en quittant la rétro

### Template compte-rendu Rétrospective

```markdown
# Rétrospective — Sprint [N]
**Date** : [date]  
**Animateur** : [Scrum Master]  
**Participants** : [liste]

## Ce qui a bien fonctionné (Continuer)
- [item 1]
- [item 2]

## Ce qui doit changer (Moins de / Arrêter)
- [item 1]
- [item 2]

## Ce qu'on veut essayer (Commencer / Plus de)
- [item 1]
- [item 2]

## Actions décidées
| Action | Responsable | Échéance |
|--------|------------|---------|
| [action 1] | [prénom] | [date] |
| [action 2] | [prénom] | [date] |

## Suivi des actions du sprint précédent
| Action | Statut |
|--------|--------|
| [action S-1] | ✅ / ❌ |
```

---

## 5. Backlog Refinement (Grooming)

**Durée** : 1 à 2 heures par semaine (max 10 % du temps du sprint)  
**Participants** : PO, Scrum Master, et au moins 2 développeurs  
**Fréquence** : Mi-sprint (environ 1 semaine avant le Sprint Planning)

### Ordre du jour

1. **Révision des US du prochain sprint** (30 min)
   - Vérification DoR pour chaque US candidate
   - Clarification des critères d'acceptation ambigus

2. **Planning Poker** (30 min)
   - Estimation des US nouvelles ou modifiées
   - Consensus par vote simultané

3. **Décomposition des grandes US** (30 min)
   - Toute US > 13 SP est décomposée
   - Vérification qu'une US peut être terminée en un sprint

4. **Priorisation** (15 min)
   - Le PO re-priorise si nécessaire en fonction des retours du sprint en cours

### Règles du Planning Poker

| Carte | Signification |
|-------|--------------|
| 1 | Trivial — quelques lignes de code |
| 2 | Très simple — moins d'une demi-journée |
| 3 | Simple — environ une journée |
| 5 | Moyen — 2 à 3 jours |
| 8 | Complexe — environ 1 semaine |
| 13 | Très complexe — limite haute acceptable |
| 21 | Trop grande — décomposer obligatoirement |
| ∞ | Trop grosse pour être estimée — décomposer |
| ? | Pas assez d'information pour estimer |

> Règle : si l'écart entre la plus haute et la plus basse estimation est ≥ 2 cartes, discussion obligatoire avant de re-voter.

---

## Calendrier type d'un sprint

| Jour | Événement |
|------|-----------|
| Lundi J1 (matin) | Sprint Planning (4h max) |
| Lundi J1 à Vendredi J10 | Daily Scrum chaque matin (15 min) |
| Mercredi J5 ou Jeudi J6 | Backlog Refinement (2h) |
| Vendredi J10 (matin) | Sprint Review (2h) |
| Vendredi J10 (après-midi) | Rétrospective (1h30) |

---

## Anti-patterns à éviter

| Anti-pattern | Problème | Solution |
|-------------|---------|---------|
| Daily Scrum de 45 minutes | Perte de temps, devient une réunion de statut | Timeboxer à 15 min, discussions techniques après |
| Sprint Planning sans DoR | US floues intègrent le sprint, travail perdu | Vérifier la DoR pour CHAQUE US |
| Rétrospective sans actions | Même problèmes reviennent | Minimum 1 action concrète avec responsable |
| PO absent de la Sprint Review | Validation impossible | PO obligatoire à la Sprint Review |
| Sprint Goal flou | L'équipe ne sait pas quoi prioriser | Sprint Goal en une phrase, affiché dans le kanban |
| Merger sans PR approuvée | Régressions non détectées | La DoD exige une PR approuvée |
