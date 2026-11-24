from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt
from .bedrock_runtime_guardrail_automated_reasoning_input_text_reference import BedrockRuntimeGuardrailAutomatedReasoningInputTextReference
from .bedrock_runtime_guardrail_automated_reasoning_statement import BedrockRuntimeGuardrailAutomatedReasoningStatement


class BedrockRuntimeGuardrailAutomatedReasoningTranslation(BaseModel):
    premises: list[BedrockRuntimeGuardrailAutomatedReasoningStatement] | None = None
    claims: list[BedrockRuntimeGuardrailAutomatedReasoningStatement] | None = None
    untranslatedPremises: list[BedrockRuntimeGuardrailAutomatedReasoningInputTextReference] | None = None
    untranslatedClaims: list[BedrockRuntimeGuardrailAutomatedReasoningInputTextReference] | None = None
    confidence: StrictFloat | StrictInt | None = None
