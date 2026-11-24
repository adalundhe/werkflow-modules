from __future__ import annotations
from pydantic import BaseModel
from .bedrock_runtime_guardrail_checks_prompt_attack_result_entry import BedrockRuntimeGuardrailChecksPromptAttackResultEntry


class BedrockRuntimeGuardrailChecksPromptAttackResult(BaseModel):
    results: list[BedrockRuntimeGuardrailChecksPromptAttackResultEntry] | None = None
