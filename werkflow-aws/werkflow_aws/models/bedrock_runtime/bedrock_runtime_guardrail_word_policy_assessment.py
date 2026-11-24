from __future__ import annotations
from pydantic import BaseModel
from .bedrock_runtime_guardrail_custom_word import BedrockRuntimeGuardrailCustomWord
from .bedrock_runtime_guardrail_managed_word import BedrockRuntimeGuardrailManagedWord


class BedrockRuntimeGuardrailWordPolicyAssessment(BaseModel):
    customWords: list[BedrockRuntimeGuardrailCustomWord] | None = None
    managedWordLists: list[BedrockRuntimeGuardrailManagedWord] | None = None
