"""
Famille testée  : Validation de sortie — options identiques forcées par injection
Payload         : sortie LLM avec 4 options identiques ("Option A" x4) sur 10 questions
Attendu avant patch : json.loads() accepte la sortie, le quiz est corrompu.
Attendu après patch : parse_and_validate_quiz() rejette les options non distinctes.
"""

import json

import pytest

from llm.services.quiz_prompt import parse_and_validate_quiz

POISONED_OUTPUT = json.dumps(
    {
        "questions": [
            {
                "prompt": f"Question {i + 1} sur le cours de physique ?",
                "options": ["Option A", "Option A", "Option A", "Option A"],
                "correct_index": 0,
            }
            for i in range(10)
        ]
    }
)


def test_t4_avant_patch_sortie_acceptee():
    """Avant patch : json.loads seul accepte les options identiques sans erreur."""
    data = json.loads(POISONED_OUTPUT)
    options = data["questions"][0]["options"]

    print("\n[T4 AVANT PATCH]")
    print(f"  Nombre d'options           : {len(options)}")
    print(f"  Options distinctes         : {len(set(options))}")
    print(f"  Contenu des options        : {options}")
    print("  => json.loads accepte sans erreur : l'injection a fonctionne")

    assert len(options) == 4
    assert len(set(options)) == 1  # toutes identiques — injection réussie


def test_t4_apres_patch_sortie_rejetee():
    """Après patch : parse_and_validate_quiz() lève une erreur sur les options identiques."""
    print("\n[T4 APRÈS PATCH]")
    with pytest.raises(Exception, match="distinctes") as exc_info:
        parse_and_validate_quiz(POISONED_OUTPUT)
    print(f"  Erreur levée : {exc_info.value}")
