# Personas — EduTutor IA

**APOCAL'IPSSI** · CADRAGE MATINAL · ARTEFACT 1 SUR 7
Projet EduTutor IA · Édition 2026 · Semaine immersive Scrum

Template : Mohamed Amine EL AFRIT (CC BY-NC-SA 4.0) — complété par l'équipe 16

---

## Identification

| Champ | Valeur |
|-------|--------|
| Equipe n° | 16 |
| Membres | Rania ZERAMDINI, Amani LAYOUNI, Badreddine CHEBBOUR, Taise de These NGANGA YABIE, Noah MASSET, Awadi BEDJA MROINKODO SAID, Clement BASTIEN |
| Sprint concerné | Cadrage |
| Version | v1.1 — intègre perturbation J1 |
| Date de remise | 30/06/2026 13h00 |
| Statut | En revue PO |

---

## Equipe Scrum

| Rôle | Responsabilités |
|------|----------------|
| Product Owner | Prioriser le backlog, définir les critères d'acceptation, valider les livrables en Sprint Review |
| Scrum Master | Animer les cérémonies, lever les obstacles, protéger l'équipe, mesurer la vélocité |
| Équipe de développement | Les 7 membres de l'équipe 16 — backend, frontend, DevOps selon compétences |

Les rôles Scrum restent distincts des rôles techniques. La même personne peut être dev backend et Scrum Master.

---

## Parties prenantes

| Partie prenante | Intérêt | Influence | Attentes |
|----------------|---------|-----------|---------|
| Équipe pédagogique IPSSI | Évaluation du projet | Haute | Cadre Scrum respecté, artefacts complets, livrables à temps |
| Étudiants (Léa Martin) | Outil de révision efficace | Forte | Quiz pertinents en < 60 s, correction immédiate, historique fiable |
| Enseignants (Mme Lefèvre) | Accompagnement pédagogique | Moyenne | Suivi de classe, tableau de bord, messagerie étudiants |
| Direction (M. David Chen) | Décision d'adoption établissement | Haute | Conformité RGPD, pérennité, rapport d'usage |
| DPO / Conformité | Protection des données | Haute | Pages légales réelles, export données, pas de LLM hors UE |

---

## Personas

Trois personas ont été identifiés pour la semaine. Ils couvrent l'ensemble des activités utilisateur décrites dans la story map. La perturbation J1 introduit Mme Sophie Lefèvre le lundi matin et étend le périmètre au-delà de l'étudiant·e.

---

### Persona 1 — Léa Martin, étudiante en L2 Droit

| Champ | Valeur |
|-------|--------|
| Nom / Prénom | Léa Martin |
| Âge | 20 ans |
| Profession | Étudiante en L2 Droit, Paris II Panthéon-Assas |
| Localisation | Paris 5e · trajet quotidien RER B 35 min |
| Situation | Boursière échelon 4, colocation 3 personnes |

#### Contexte d'usage

Léa révise principalement en soirée (19h–22h) et le dimanche après-midi. Elle utilise son smartphone Android pour la plupart de ses usages numériques et emprunte un laptop à la BU deux fois par semaine — elle n'a pas d'ordinateur personnel. Son volume de révision est d'environ 8h par semaine, dont 3h sont perdues à chercher des supports de qualité aléatoire.

Elle est autonome sur Moodle et l'ENT de son université, a testé ChatGPT 4 à 5 fois pour des résumés sans en faire un usage régulier, et est allergique aux installations CLI ou paramétrages techniques avancés.

#### Ce qui la bloque

- Perd ~3h/semaine à chercher des fiches de révision en ligne — qualité très aléatoire
- Les fiches trouvées ne sont jamais à jour avec son programme (les cours changent chaque année)
- Se sent surchargée à 3 semaines des partiels, sans plan de révision personnalisé
- Ne sait pas mesurer si elle "connaît" un chapitre ou si elle "croit" le connaître
- Échoue à 2 chapitres/semestre par manque d'auto-évaluation précoce, pas par manque de travail

#### Objectifs

- Générer un quiz de révision sur n'importe quel chapitre en moins de 5 minutes
- Identifier ses lacunes par chapitre 2 semaines avant les partiels (vs 3 jours avant aujourd'hui)
- Gagner ~2h/semaine sur la recherche de supports
- Obtenir un retour immédiat sur ses réponses pour corriger ses erreurs le soir même

#### Critères de succès

- "Si je gagne au moins 1h/semaine sur ma préparation, j'adopte."
- "Si ça plante 1 fois en bibliothèque devant mes amies, je n'y reviens jamais."
- "Si l'app me dit exactement quel chapitre retravailler avant mes partiels, je la recommande à toute ma promo."

#### Stories associées

MUST : US-01, US-02, US-03, US-04, US-05, US-06
SHOULD : US-07, US-08, US-09, US-10, US-11, US-12
COULD : US-13, US-14, US-16, US-17

---

### Persona 2 — Mme Sophie Lefèvre, enseignante en BTS Communication

| Champ | Valeur |
|-------|--------|
| Nom / Prénom | Mme Sophie Lefèvre |
| Âge | 42 ans |
| Profession | Professeure de Communication, BTS, lycée privé sous contrat |
| Localisation | Lyon · trajet voiture 25 min · établissement Lyon 6e |
| Situation | Mariée, 2 enfants (12 et 15 ans), salaire ~2 700 € net/mois |

#### Contexte d'usage

Sophie a 28 étudiants dans sa classe BTS Communication 1ère année. Elle consacre 6h de cours par semaine, 3h de préparation et 3h de correction, soit 12h de travail pédagogique hebdomadaire. La salle informatique de l'établissement est disponible mais le réseau est lent (4G partagée). Les étudiants ont des smartphones Android personnels de générations variées.

Elle utilise Moodle pour déposer ses cours mais n'a jamais créé de quiz en ligne : tout se fait sur papier. Elle est power user Word + Excel, autonome sur Moodle et Pronote, mais abandonne si une configuration demande plus de 3 étapes. Elle découvre l'IA générative (2 essais ChatGPT, résultat jugé "trop générique").

Elle n'est pas une observatrice passive. Elle veut être une actrice de la plateforme : générer elle-même des quiz à partir de ses cours, les partager à sa classe, voir qui a répondu et où chacun accroche, et intervenir directement auprès des étudiants en difficulté sans attendre le cours suivant.

#### Ce qui la bloque

- Corrige 28 copies × 3 quiz/semaine = ~12h de correction/mois rien que pour les quiz
- Créer 1 quiz cohérent prend ~90 minutes de préparation
- Pas de variation des questions : les étudiants se passent les réponses entre promo
- Aucun tableau de bord — impossible de savoir quels chapitres posent problème sans relire toutes les copies

#### Objectifs

- Générer 1 quiz personnalisé en moins de 5 minutes sur n'importe quel chapitre
- Suivre l'engagement de la classe (qui a répondu, score moyen, lacunes communes)
- Réduire le temps de correction de 12h à moins de 3h/mois grâce à la correction automatique
- Voir d'un coup d'œil quels élèves n'ont pas répondu

#### Critères de succès

- "Si je gagne 1h/semaine sur ma préparation, j'adopte définitivement."
- "Si ça plante 1 fois en cours devant 28 ados, je n'y reviens jamais."
- "Si je vois d'un coup d'œil quels élèves n'ont pas répondu, je gagne un temps fou en relances."

#### Contrainte de périmètre — aucune story MUST

Sophie arrive comme perturbation J1 le lundi matin. Son besoin est réel et stratégique, mais il arrive en milieu de cadrage. Aucune de ses stories n'est MUST : le parcours étudiant F1–F6 reste la priorité de Release 1. L'interface admin existante (/admin) couvre partiellement US-21 sans développement (COULD R1). US-22 est SHOULD R2. US-23 est COULD R2.

#### Stories associées

COULD R1 : US-21
SHOULD R2 : US-22
COULD R2 : US-15, US-23

---

### Persona 3 — M. David Chen, directeur des études

| Champ | Valeur |
|-------|--------|
| Nom / Prénom | M. David Chen |
| Âge | 51 ans |
| Profession | Directeur des études, lycée privé sous contrat (1 200 élèves) |
| Localisation | Lyon 6e · même établissement que Mme Lefèvre |
| Situation | Marié, enfants grands, 25 ans d'expérience dans l'enseignement |

#### Contexte d'achat

M. Chen gère un budget edtech de ~12 000 €/an pour son lycée (10 €/élève × 1 200). Son cycle d'achat est de 6 mois minimum — il faut la validation pédagogique, le DPO et la comptabilité. Il choisit les outils edtech une fois par an, en mai/juin pour la rentrée de septembre, en concertation avec le conseil pédagogique, le DPO et le gestionnaire financier.

Il a déjà refusé 2 outils en 2024 faute de garanties RGPD suffisantes, même après démonstration convaincante. Son DPO refuse systématiquement les outils utilisant OpenAI ou des LLM US (transferts hors UE). Il est sous pression du CA pour démontrer une "stratégie IA pédagogique" sans compromettre la conformité légale.

#### Ce qui le bloque

- DPO refuse les outils utilisant des LLM américains (hébergement hors UE)
- A déjà signé pour 2 outils edtech qui ont fermé en cours d'année (risque pérennité)
- Les profs râlent quand on impose un nouvel outil sans les consulter
- Aucun outil actuel ne lui fournit de rapport d'usage consolidé pour justifier le budget au CA

#### Objectifs

- Disposer d'un outil edtech IA RGPD conforme, signable sans risque juridique
- Tarification prévisible par élève/an, sans surprise au renouvellement
- Adhésion d'au moins 30 % des profs dès la première année
- Obtenir un rapport d'usage trimestriel exportable pour présenter au CA

#### Critères de succès

- "Si le DPO valide les CGV en 30 min de lecture, c'est un signal positif."
- "Si 5 profs me demandent spontanément d'élargir l'usage, je signe le renouvellement."
- "Si je reçois un rapport d'usage automatique chaque trimestre, je n'ai plus à justifier manuellement le budget."

#### Périmètre semaine

M. Chen représente la vision long terme B2B. Ses exigences conditionnent la Release 1 sur le plan RGPD (US-12 export données, pages légales) et orientent les stories WON'T (SSO SAML/OIDC = hors périmètre semaine, cible B2B post-prototype).

#### Stories associées

SHOULD R2 : US-12 (export RGPD Art. 15)
WON'T : US-18 (SSO SAML/OIDC)

---

## Synthèse

| Persona | Rôle | MUST | SHOULD | COULD | WON'T |
|---------|------|------|--------|-------|-------|
| Léa Martin (étudiante) | Cœur de cible R1 | US-01 à US-06 | US-07 à US-12 | US-13, US-14, US-16, US-17 | US-19, US-20 |
| Mme Lefèvre (enseignante) | Cible J1 — aucun MUST | aucune | US-22 | US-15, US-21, US-23 | — |
| M. David Chen (direction) | Vision long terme B2B | aucune | US-12 | — | US-18 |

Le périmètre de la semaine est centré sur Léa. Mme Lefèvre oriente Release 2 et les stories J1. M. David Chen oriente les exigences RGPD et les décisions WON'T.

---

## Anti-personas (hors cible)

Trois profils sont explicitement exclus du périmètre :

- Élève de primaire ou collège (moins de 15 ans) : EduTutor IA repose sur la capacité à fournir un cours structuré et à interpréter un feedback d'auto-évaluation de manière autonome. Ce niveau d'autonomie n'existe pas avant le lycée.
- Enseignant·e du primaire ou retraité·e en autoformation : le besoin de Mme Lefèvre (évaluations à grande échelle, suivi de groupe) n'existe pas pour un usage individuel ou un volume de quelques élèves.
- Établissement sans contrainte RGPD orienté LLM américain : la différenciation d'EduTutor IA est le local-first et la souveraineté des données. Courir après ce marché affaiblirait le positionnement différenciateur.
