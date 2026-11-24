from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .bedrock_runtime_guardrail_checks_content_block import BedrockRuntimeGuardrailChecksContentBlock


class BedrockRuntimeGuardrailChecksMessage(BaseModel):
    role: Literal['user', 'assistant', 'system']
    content: list[BedrockRuntimeGuardrailChecksContentBlock]
