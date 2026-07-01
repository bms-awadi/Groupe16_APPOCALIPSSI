"""
Famille testée  : Injection directe naïve
Payload         : fichier cours contenant "IGNORE TOUTES LES INSTRUCTIONS PRÉCÉDENTES"
                  en clair dans le corps du texte (fixtures/t1_direct_injection.txt)
Attendu avant patch : le texte malveillant passe tel quel dans le prompt.
Attendu après patch : sanitize_source() met IGNORE en minuscules.
"""

from pathlib import Path

from llm.services.quiz_prompt import sanitize_source

FIXTURE = Path(__file__).parent / "fixtures" / "t1_direct_injection.txt"


def test_t1_avant_patch_injection_visible():
    """Avant patch : sans sanitization, IGNORE reste en majuscules dans le prompt."""
    source = FIXTURE.read_text(encoding="utf-8")
    raw_prompt = f"COURS :\n{source}\n\nGÉNÈRE LE JSON MAINTENANT :"

    print("\n[T1 AVANT PATCH]")
    print(f"  Payload trouvé dans le prompt : {'IGNORE' in raw_prompt}")
    idx = raw_prompt.find("IGNORE")
    print(f"  Extrait : ...{raw_prompt[max(0,idx-10):idx+50]}...")

    assert "IGNORE" in raw_prompt


def test_t1_apres_patch_injection_bloquee():
    """Après patch : sanitize_source() neutralise IGNORE en majuscules."""
    source = FIXTURE.read_text(encoding="utf-8")
    result = sanitize_source(source)

    print("\n[T1 APRÈS PATCH]")
    print(f"  'IGNORE' en majuscules présent : {'IGNORE' in result}")
    print(f"  'ignore' en minuscules présent : {'ignore' in result.lower()}")

    assert "IGNORE" not in result
    assert "ignore" in result.lower()
