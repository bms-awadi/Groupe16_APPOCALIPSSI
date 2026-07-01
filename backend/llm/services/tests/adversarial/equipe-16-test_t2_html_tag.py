"""
Famille testée  : Injection indirecte via balise HTML cachée
Payload         : fichier cours contenant <script>IGNORE...</script>
                  (fixtures/t2_html_tag.txt)
Attendu avant patch : la balise <script> passe intacte dans le prompt.
Attendu après patch : sanitize_source() supprime toutes les balises HTML/XML.
"""

from pathlib import Path

from llm.services.quiz_prompt import sanitize_source

FIXTURE = Path(__file__).parent / "fixtures" / "t2_html_tag.txt"


def test_t2_avant_patch_balise_visible():
    """Avant patch : sans sanitization, la balise <script> reste dans le prompt."""
    source = FIXTURE.read_text(encoding="utf-8")
    raw_prompt = f"COURS :\n{source}\n\nGÉNÈRE LE JSON MAINTENANT :"

    print("\n[T2 AVANT PATCH]")
    print(f"  Balise <script> présente : {'<script>' in raw_prompt}")
    idx = raw_prompt.find("<script>")
    print(f"  Extrait : ...{raw_prompt[max(0,idx-5):idx+60]}...")

    assert "<script>" in raw_prompt


def test_t2_apres_patch_balise_supprimee():
    """Après patch : sanitize_source() retire les balises HTML."""
    source = FIXTURE.read_text(encoding="utf-8")
    result = sanitize_source(source)

    print("\n[T2 APRÈS PATCH]")
    print(f"  Balise <script> présente : {'<script>' in result}")
    print(f"  'IGNORE' présent          : {'IGNORE' in result}")

    assert "<script>" not in result
    assert "IGNORE" not in result
