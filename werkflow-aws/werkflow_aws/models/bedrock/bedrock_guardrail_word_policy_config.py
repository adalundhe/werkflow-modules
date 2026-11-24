from __future__ import annotations
from pydantic import BaseModel
from .bedrock_guardrail_managed_words_config import BedrockGuardrailManagedWordsConfig
from .bedrock_guardrail_word_config import BedrockGuardrailWordConfig


class BedrockGuardrailWordPolicyConfig(BaseModel):
    wordsConfig: list[BedrockGuardrailWordConfig] | None = None
    managedWordListsConfig: list[BedrockGuardrailManagedWordsConfig] | None = None
