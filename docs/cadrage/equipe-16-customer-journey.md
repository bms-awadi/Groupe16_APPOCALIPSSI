# CUSTOMER JOURNEY MAPS – EduTutor IA

**Sprint:** Cadrage  
**Version:** v1.1  
**Date de remise:** 29/06/2026  
**Statut:** En revue PO  
**Équipe n°:** 16 
**Membres:** Rania ZERAMDINI, Amani LAYOUNI, Badreddine CHEBBOUR, Taise de Thèse NGANGA YABIE, Awadi BEDJA MROINKODO SAID, Clément BASTIEN

---

## PARCOURS 1 : LÉA MARTIN (Étudiante - CIBLE PRIMAIRE)

| Étape | Actions | Pensées | Émotion | Frictions | Opportunités |
|-------|---------|----------|---------|-----------|-------------|
| **1. Découverte** | Voit une story Instagram d'une influenceuse étudiante. Clique sur le lien. | "Encore un outil qui promet la lune ? Mais j'ai un partiel dans 2 sem, ça vaut le coup d'essayer." | Curieuse, sceptique | Landing page trop technique, trop de jargon IA | Témoignages étudiants authentiques, preuve sociale de vraies notes avant/après |
| **2. Inscription** | Crée un compte avec son email universitaire. Mot de passe Bitwarden. | "Au moins ils demandent pas mon numéro de téléphone... RGPD respecté ?" | Vigilante | Pas d'option SSO Google/Apple (obligée de créer compte spécifique) | Mention RGPD claire pendant inscription, badge "Confidentiel" visible |
| **3. 1ère utilisation** | Upload PDF de droit constitutionnel (340 pages). Clique "Générer quiz" chap. 4. | "340 pages... j'espère que ça va pas planter. Pourquoi pas de barre de progression ?" | Anxieuse → Soulagée | Pas d'indicateur progression pendant 30+ secondes, écran vide = stress | Message rassurant "Quiz en cours de génération...", barre progression animée, spinner |
| **4. Usage régulier** | Génère 3 quiz/sem sur 5 chapitres pendant 2 sem avant les partiels. | "J'ai gagné au moins 2h/sem. Je me sens bien plus prête maintenant." | Confiante, satisfaite | Pas d'accès historique hors-ligne (besoin wifi dans RER) | Sync hors-ligne des quiz déjà passés, mode avion-friendly |
| **5. Recommandation** | Partage le lien à 3 amies de promo dans groupe WhatsApp. | "Si ça les aide elles aussi, on pourrait faire des sessions de révision communes." | Enthousiaste | Pas de fonction partage de quiz entre comptes (doit repartager le lien) | Mode groupe/promo avec partage de quiz, sessions communes |


---

## PARCOURS 2 : MME SOPHIE LEFÈVRE (Enseignant·e - CIBLE SECONDAIRE)

| Étape | Actions | Pensées | Émotion | Frictions | Opportunités |
|-------|---------|---------|---------|-----------|---------------|
| **1. Découverte** | Lit article du Café Pédagogique sur outils IA. Note le nom EduTutor. | "Encore une promesse marketing ? Je veux des exemples concrets pour BTS Communication." | Curieuse, prudente | Pas d'exemples sectoriels (BTS vs lycée vs sup : contextes très différents) | Démos par niveau, études de cas BTS réels, témoignages profs secteur |
| **2. Inscription** | Demande compte enseignant via formulaire contact. Attend 48h une réponse. | "48h pour répondre ? S'ils ne sont pas réactifs en amont, comment ce sera en SAV ?" | Impatiente (DÉCROCHAGE) | Pas d'auto-inscription prof, validation manuelle = délai > 24h | Compte gratuit auto-créé en 2 min, onboarding 5 min, parrainage écoles |
| **3. 1ère utilisation** | Upload cours Communication non-verbale. Génère 1 quiz test pour voir. | "Si les questions sont mal formulées ou fausses, je n'y reviens pas. Je dois pouvoir vérifier." | Vigilante → Étonnée | Pas d'aperçu rapide des questions avant publication en classe | Mode preview avant publication, pouvoir modifier questions individuelles |
| **4. Usage régulier** | Génère 3 quiz/sem pour ses 28 étudiants. Adapte niveau selon retours. | "J'ai gagné 4h/sem sur préparation ! Mais je veux pouvoir corriger une question fausse rapidement." | Satisfaite, productive | Pas d'édition manuelle après génération (doit tout régénérer) | Éditeur intégré pour corriger 1 question rapidement sans régénérer |
| **5. Recommandation (direction)** | Présente l'outil conseil pédagogique. Demande budget pour passage B2B. | "Si direction signe, je veux prouver le ROI : 4h/sem × 30 sem × 5 profs = 600h/an gagnées." | Convaincue, militante | Pas de dashboard ROI exportable pour présenter à direction | Rapport mensuel automatique : ROI chiffré, temps gagné, adoption élèves |


---

## PARCOURS 3 : M. DAVID CHEN (Établissement B2B - CIBLE TERTIAIRE)

| Étape | Actions | Pensées | Émotion | Frictions | Opportunités |
|-------|---------|----------|---------|-----------|-------------|
| **1. Découverte besoin** | CA demande stratégie IA pédagogique. Mme Lefèvre en parle au conseil. | "Le CA pousse sur l'IA, mais pas question de signer avec OpenAI. Données élèves = confidentiel." | Prudent, sous pression | Pas de garantie RGPD écrite visible, crainte transferts données UE | Fiche RGPD prête à l'emploi, mention "Local-first" bien visible, lettre cabinet jur. |
| **2. Évaluation** | Envoie CGV au DPO mutualisé. Demande démo. Compare 3 outils en parallèle. | "Si le DPO valide les CGV en 30 min, c'est un signal très positif pour la viabilité." | Méticuleux, analytique | DPO en congés 3 semaines, CGV pas prêtes à temps, validation lente | Check-list RGPD pré-validée cabinet jur, CGV prêtes, réponse 24h garantie |
| **3. Décision** | Signe contrat annuel 1 200 élèves × 10€/élève. Valide déploiement. | "Si dans 6 mois je dois reculer, ça sera politiquement très coûteux. Mieux sécuriser maintenant." | Engagé, un peu anxieux | Pas de clause d'essai 3 mois, engagement immédiat = risque | Période pilote gratuite 3 mois avant signature, step-wise onboarding |
| **4. Onboarding équipe** | Présente l'outil aux 40 profs. Forme 5 ambassadeurs. Distribue comptes. | "Si dès la 1ère semaine les profs râlent que ça plante, j'ai perdu l'année." | Espérant → Soulagé | Pas de matériel de formation prêt, documentation sommaire, support limité | Kit déploiement clé en main (slides, vidéos, FAQ, hotline 48h) |
| **5. Renouvellement** | Mesure adoption fin an 1 : 35% profs actifs, 80% élèves ont utilisé ≥ 1x. | "35% adoption profs = au-dessus du seuil 30%. Je peux dire au CA on est en avance sans mentir." | Confiant, fier | Pas de comparaison benchmark avec autres écoles (impression d'isolement) | Benchmark sectoriel anonyme, rapport comparatif, best practices pairs |
