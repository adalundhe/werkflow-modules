from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bedrock_runtime_guardrail_automated_reasoning_statement import BedrockRuntimeGuardrailAutomatedReasoningStatement


class BedrockRuntimeGuardrailAutomatedReasoningLogicWarning(BaseModel):
    type: StrictStr | None = None
    premises: list[BedrockRuntimeGuardrailAutomatedReasoningStatement] | None = None
    claims: list[BedrockRuntimeGuardrailAutomatedReasoningStatement] | None = None
