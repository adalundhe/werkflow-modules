from __future__ import annotations
from pydantic import BaseModel
from .bedrock_guardrail_managed_words import BedrockGuardrailManagedWords
from .bedrock_guardrail_word import BedrockGuardrailWord


class BedrockGuardrailWordPolicy(BaseModel):
    words: list[BedrockGuardrailWord] | None = None
    managedWordLists: list[BedrockGuardrailManagedWords] | None = None
