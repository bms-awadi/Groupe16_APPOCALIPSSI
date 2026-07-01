"""
Famille testée  : Validation de sortie — JSON incomplet (moins de 10 questions)
Payload         : sortie LLM avec une seule question au lieu de 10
Attendu avant patch : json.loads() accepte la liste tronquée sans vérification.
Attendu après patch : parse_and_validate_quiz() lève une LLMError.
"""

import json

import pytest

from llm.services.quiz_prompt import parse_and_validate_quiz

TRUNCATED_OUTPUT = json.dumps(
    {
        "questions": [
            {
                "prompt": "Question unique sur le cours ?",
                "options": ["Réponse A", "Réponse B", "Réponse C", "Réponse D"],
                "correct_index": 0,
            }
        ]
    }
)


def test_t5_avant_patch_sortie_acceptee():
    """Avant patch : json.loads seul accepte 1 question sans vérifier le compte."""
    data = json.loads(TRUNCATED_OUTPUT)

    print("\n[T5 AVANT PATCH]")
    print(f"  Nombre de questions reçues : {len(data['questions'])}")
    print(f"  Nombre attendu             : 10")
    print("  => json.loads accepte sans erreur : le quiz est incomplet en base")

    assert len(data["questions"]) == 1  # structurellement valide mais incomplet


def test_t5_apres_patch_sortie_rejetee():
    """Après patch : parse_and_validate_quiz() lève une erreur si < 10 questions."""
    print("\n[T5 APRÈS PATCH]")
    with pytest.raises(Exception, match="questions") as exc_info:
        parse_and_validate_quiz(TRUNCATED_OUTPUT)
    print(f"  Erreur levée : {exc_info.value}")
