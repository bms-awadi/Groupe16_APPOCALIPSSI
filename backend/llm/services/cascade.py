"""
Cascade de repli LLM — ADR-0001 (J2).

Ordre de tentative :
  1. Groq llama-3.1-8b-instant     (primaire  — ~1s)
  2. Ollama llama3.1:8b GPU        (repli 1   — ~7s)
  3. Groq llama-3.3-70b-versatile  (repli 2   — ~2s)
  4. Ollama phi GPU                (repli 3   — ~12s)

Utilisée automatiquement quand le backend configuré est « groq ».
Les autres backends (mock, ollama direct, etc.) court-circuitent la cascade.
"""

import logging

from django.conf import settings

from .base import LLMError
from .groq_client import GroqLLMClient
from .ollama_client import OllamaLLMClient

logger = logging.getLogger(__name__)

_CLOUD_TIMEOUT = 30  # secondes avant bascule vers le repli suivant


def _chain(api_key: str, ollama_host: str | None) -> list[tuple[str, object]]:
    """Retourne la liste ordonnée (label, client) de la cascade ADR-0001."""
    groq_key = api_key or getattr(settings, "GROQ_API_KEY", "")
    host = ollama_host or None
    return [
        (
            "Groq llama-3.1-8b-instant (primaire)",
            GroqLLMClient(api_key=groq_key, model="llama-3.1-8b-instant", timeout=_CLOUD_TIMEOUT),
        ),
        (
            "Ollama llama3.1:8b GPU (repli 1)",
            OllamaLLMClient(model="llama3.1:8b", host=host),
        ),
        (
            "Groq llama-3.3-70b-versatile (repli 2)",
            GroqLLMClient(api_key=groq_key, model="llama-3.3-70b-versatile", timeout=_CLOUD_TIMEOUT),
        ),
        (
            "Ollama phi GPU (repli 3)",
            OllamaLLMClient(model="phi", host=host),
        ),
    ]


def generate_quiz_with_cascade(
    source_text: str,
    title: str,
    api_key: str = "",
    ollama_host: str = "",
) -> list[dict]:
    """Génère un quiz en essayant chaque backend dans l'ordre de la cascade.

    Bascule automatiquement sur le repli suivant à chaque LLMError ou exception
    réseau. Lève LLMError si tous les backends ont échoué.
    """
    last_exc: Exception | None = None

    for label, client in _chain(api_key, ollama_host):
        try:
            logger.info("[LLM cascade] Tentative : %s", label)
            result = client.generate_quiz(source_text=source_text, title=title)
            logger.info("[LLM cascade] Succès : %s", label)
            return result
        except Exception as exc:
            logger.warning(
                "[LLM cascade] Échec %s — passage au repli suivant. Cause : %s",
                label,
                exc,
            )
            last_exc = exc

    raise LLMError(f"Tous les backends LLM ont échoué. Dernière erreur : {last_exc}")
