from __future__ import annotations
from pydantic import BaseModel
from .bedrock_runtime_guardrail_automated_reasoning_statement import BedrockRuntimeGuardrailAutomatedReasoningStatement


class BedrockRuntimeGuardrailAutomatedReasoningScenario(BaseModel):
    statements: list[BedrockRuntimeGuardrailAutomatedReasoningStatement] | None = None
