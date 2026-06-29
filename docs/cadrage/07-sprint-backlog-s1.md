# Sprint Backlog S1

## Objectif

À la fin du sprint, un étudiant doit pouvoir s'inscrire, uploader son cours, générer un quiz, le passer, voir son score et retrouver tout ça dans son historique, le parcours complet F1-F6 doit être stable.

---

## Ce qu'on s'engage à faire

| ID | User Story | SP | Binôme |
|----|------------|----|--------|
| US-01 | Finaliser l'inscription par email + tests | 2 | A — Auth |
| US-02 | Finaliser la validation d'email + tests | 1 | A — Auth |
| US-03 | Finaliser la connexion + tests | 1 | A — Auth |
| US-15 | Finaliser le reset mot de passe + tests | 1 | A — Auth |
| US-16 | Page profil (modifier / supprimer compte) | 2 | A — Auth |
| US-04 | Finaliser l'upload PDF (≤ 5 Mo) + cas limites | 2 | B — Contenu |
| US-05 | Finaliser la saisie texte (≥ 200 caractères) | 1 | B — Contenu |
| US-06 | Ajuster le prompt LLM pour 10 QCM + tests | 3 | C — Quiz |
| US-07 | Finaliser le passage du quiz interactif | 2 | C — Quiz |
| US-08 | Finaliser le score /10 et la correction | 1 | D — Résultat |
| US-09 | Historique des quiz par utilisateur | 2 | D — Résultat |

**Total : 18 SP** (on garde 6 SP de marge pour les imprévus)

---

- F1 (auth complète) : couvert par US-01, 02, 03, 15, 16
- F2 (upload) : couvert par US-04, 05
- F3 (génération LLM) : couvert par US-06
- F4 (passage + correction) : couvert par US-07, 08
- F5 (score /10) : couvert par US-08
- F6 (historique) : couvert par US-09
---

## Dépendances

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
- `make test` passe sans régression
- `make lint` passe
- On peut faire une démo en 2 min du parcours complet (inscription → upload → quiz → score → historique)
- Retrospective de 15 min avant la perturbation P2
