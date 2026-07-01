# ADR-01 : Bascule du backend LLM pour la génération de quiz

**Numéro**  :  ADR-0001 
**Équipe n°**  : 16 (APOCAL'IPSSI 2026) 
**Titre** : Bascule latence génération de quiz : Ollama Llama 3.1 8B CPU -> Hybride Groq Instant 
(cloud) + Ollama Llama 3.1 8B GPU (repli) 
**Membres**  : Rania ZERAMDINI, Amani LAYOUNI, Badreddine CHEBBOUR, Taise de Thèse 
NGANGA YABIE, Awadi BEDJA MROINKOKO SAID, Clément BASTIEN 
**Version**  : v1.0  
**Date** : 30/06/2026 (J2) 
**Statut**  : Prêt pour validation PO

---

## 1. Reformulation du problème

Retour beta-test (PO, 01/07 10h00) : un étudiant de M2 a uploadé un cours d'algorithmique et attendu **45 secondes** pour obtenir 10 questions. Il a cru l'application cassée et a failli abandonner : *« Si chaque quiz est aussi long, c'est inutilisable. »* Le sponsor exige une latence de génération acceptable **d'ici ce soir** (démo MVP Release 1, 17h45) et une solution documentée.

Reformulé techniquement : le pipeline de génération de quiz repose actuellement sur **Ollama Llama 3.1 8B exécuté en CPU**, dont la latence mesurée en conditions contrôlées est **p50 = 124.95s** (voir §2). Cette valeur est très supérieure au seuil d'acceptabilité utilisateur retenu (≤ 15s, critère d'acceptation CA-J2-6) et confirme le ressenti du testeur.

L'écart entre le retour terrain (45s) et la mesure formelle (124.95s) s'explique probablement par un cours plus court soumis par le testeur et/ou une machine différente de celle du benchmark ; dans les deux cas le diagnostic converge vers la même conclusion.

Le problème n'est donc **pas la qualité du modèle** (jugée correcte, ~8/10 en évaluation subjective) mais l'**environnement d'exécution** (CPU vs GPU) et le **choix d'un provider local vs cloud**. Objectif : ramener la latence sous 15s sans sacrifier la qualité des quiz générés, avant la démo de ce soir.

---

## 2. Contexte

### 2.1. Situation factuelle — mesures réelles (CPU + GPU)

**Baseline CPU — Ollama Llama 3.1 8B (sans GPU)**
- Latence p50 : **124.95s**
- Latence min / max : 112.57s / 146.89s
- Verdict : **inacceptable**

**Ollama avec GPU (NVIDIA RTX 4070)**
- Llama 3.1 8B (GPU) : **6.85s** (94.5% de gain vs CPU), 4/5 runs valides
- Phi (GPU) : **11.72s** (91.3% de gain vs CPU)
- Mistral (GPU) : **20.17s** (87.5% de gain vs CPU)
- Neural Chat (GPU) : **25.09s** (86.7% de gain vs CPU)

**Cloud — Groq Llama 3.1 8B Instant**
- Latence p50 : **1.08s**
- Latence min / max : 0.95s / 1.22s (variance 0.27s)
- Gain : **99.1%** vs baseline CPU
- 5/5 runs valides, résultat stable

**Cloud — Groq Llama 3.3 70B**
- Latence p50 : **2.35s**, 5/5 runs valides — alternative cloud si Instant throttle

*Protocole détaillé (nombre de runs par configuration, cours de référence utilisé, spécifications machine) : voir le document séparé Benchmark méthodologique. Cette ADR résume les résultats, pas le protocole complet.*

### 2.2. Tableau comparatif complet

| Modèle | CPU (p50) | GPU RTX 4070 (p50) | Cloud Groq (p50) | Meilleur environnement |
|---|---|---|---|---|
| Groq Instant | — | — | **1.08s** | ✅ Gagnant global |
| Llama 3.1 8B | 124.95s | 6.85s | — | ✅ GPU viable en repli |
| Phi | 134.27s | 11.72s | — | Repli possible |
| Mistral | 161.01s | 20.17s | — | Repli possible |
| Neural Chat | 188.19s | 25.09s | — | Repli possible |
| Llama 3.3 70B | — | — | 2.35s | Alternative cloud |

### 2.3. Impact si aucune décision n'est prise

- MVP Release 1 (démo de ce soir, 17h45) rejeté : 124.95s est très au-dessus du seuil d'acceptabilité (≤15s).
- Risque d'abandon utilisateur élevé, conforme au retour terrain du testeur M2.

### 2.4. Contraintes du projet

- Stack existante : Ollama en local, GPU disponible sur au moins une machine de l'équipe.
- Délai : décision et premiers correctifs attendus avant ce soir ; Sprint 2 démarre jeudi 14h.
- Conformité : RGPD à maintenir (données de cours potentiellement sensibles).

---

## 3. Options envisagées

| Option | Latence | Avantages | Inconvénients | Effort | Risque |
|---|---|---|---|---|---|
| **A. Ne rien faire (CPU)** | 124.95s | Zéro effort | Démo rejetée, adoption compromise | — | Très élevé |
| **B. Ollama local + GPU** | 6.85s | Gratuit, RGPD ok, 100% local | Dépend du GPU de la machine utilisée | ~1h | Faible |
| **C. Groq Instant (cloud)** | 1.08s | Ultra-rapide, free tier | Dépendance à une API externe | ~4h | Très faible |
| **D. Hybride : Groq + Ollama GPU** | 1.08s / 6.85s | Meilleure latence + repli local sans dépendance réseau | Stack plus complexe (cascade de fallback) | ~6h | Faible |

---

## 4. Décision retenue

**→ Option D : hybride — Groq Instant en primaire, Ollama GPU et modèles secondaires en cascade de repli.**

- **Primaire** : Groq Llama 3.1 8B Instant (1.08s) — prêt pour la production
- **Repli 1** : Ollama Llama 3.1 8B GPU local (6.85s) — si Groq indisponible ou en quota
- **Repli 2** : Groq Llama 3.3 70B (2.35s) — si le GPU local n'est pas disponible (ex. démo sur une machine sans GPU dédié)
- **Repli 3** : Phi GPU (11.72s) — dernier recours si tout le cloud Groq est indisponible et qu'un GPU est disponible

### 4.1. Justification

**Groq Instant est le meilleur choix mesuré** : 1.08s p50, gain de 99.1% vs baseline CPU, 5/5 runs valides avec une variance faible (0.27s) — la latence la plus basse et la plus fiable des options testées.

**Ollama GPU local (6.85s)** constitue un excellent filet de sécurité : gain de 94.5% vs CPU, gratuit, 100% RGPD, aucune dépendance réseau. Il ne remplace pas Groq mais garantit une continuité de service si le cloud est indisponible.

**Qualité** : Llama 3.1 8B évalué ~8/10 en qualité subjective, jugée équivalente à la baseline — la bascule ne dégrade pas l'expérience utilisateur sur le fond, seulement la forme (latence).

### 4.2. Mesures de mitigation

**Risque 1 — Indisponibilité de Groq (tous modèles)**
- Feature flag `LLM_BACKEND=groq | groq-llama33 | ollama-gpu | phi-gpu` avec cascade de fallback automatique.
- Timeout 30s avant bascule vers le repli suivant.

**Risque 2 — GPU local indisponible** (ex. démo sur une machine sans GPU dédié)
- Bascule vers **Groq Llama 3.3 70B** (repli 2), et non vers Groq Instant : si on en est à ce repli, c'est que Groq Instant a déjà été tenté et a échoué, ou que le contexte impose un autre chemin ; revenir sur le même service n'a pas de sens.
- Dans tous les cas, **aucun scénario ne doit retomber sur le CPU seul** (124.95s, inacceptable).

**Risque 3 — Conformité RGPD**
- Ollama local : 100% RGPD, aucune donnée ne quitte la machine.
- Groq (cloud) : la politique de non-réutilisation des données pour l'entraînement et le délai de suppression annoncés (24h) doivent être **confirmés dans la documentation officielle de Groq avant mise en production** — non vérifiés à ce stade de rédaction de cette ADR.

---

## 5. Conséquences

### 5.1. Positives (mesurées)

- Latence p50 : 124.95s → 1.08s (Groq) ou 6.85s (repli GPU) = gain 99.1% / 94.5%.
- Démo garantie : latence < 7s dans 100% des scénarios de repli (hors panne totale).
- Qualité : Llama 3.1 8B ~8/10, identique à la baseline.
- Coût : free tier Groq, estimation < 1 USD/mois.
- Cascade de repli à 4 niveaux couvrant panne cloud, panne GPU, et throttling.

### 5.2. Négatives (assumées)

- Dépendance à une API cloud tierce (Groq) pour le chemin primaire.
- Dépendance au GPU de la machine de démo pour le premier niveau de repli.
- Complexité accrue de la stack (4 backends en cascade à maintenir et tester).
- Conformité RGPD de Groq encore à confirmer formellement (voir §4.2, risque 3).

---

## 6. KPIs à surveiller

| KPI | Seuil cible | Seuil d'alerte | Action si alerte |
|---|---|---|---|
| Latence p50 | < 2s | > 3s | Re-benchmark, vérifier le backend actif |
| Taux de succès Groq (Instant) | ≥ 95% | < 90% | Bascule automatique vers repli Ollama GPU |
| Taux de succès Ollama GPU | ≥ 90% | < 85% | Bascule vers Groq 3.3 70B |
| Score de qualité subjective | ≥ 7.5/10 | < 7/10 | Revoir le prompt de génération |

**Date de revue de cette ADR** : 10 jours après mise en production.

---

## Résumé exécutif

**Problème** : Ollama CPU = 124.95s, très au-dessus du seuil d'acceptabilité (≤15s), confirmé par un retour utilisateur négatif.

**Décision** : bascule hybride — Groq Instant (1.08s) en primaire, Ollama GPU (6.85s) en repli local, avec cascade de secours supplémentaire (Groq 3.3 70B, Phi GPU).

**Gain** : 99.1% (Groq) / 94.5% (Ollama GPU) vs baseline CPU.

**Coût** : free tier Groq (<1 USD/mois).

**Risque résiduel** : faible, sous réserve de confirmation de la politique de données Groq (RGPD).

**Prochaine étape** : implémentation Sprint 2 (jeudi 14h) ; Sprint Backlog à mettre à jour en parallèle (tâches d'investigation + bascule, re-estimation des stories impactées avant/après).
