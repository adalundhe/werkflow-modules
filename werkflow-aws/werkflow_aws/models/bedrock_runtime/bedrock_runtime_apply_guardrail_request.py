from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .bedrock_runtime_guardrail_content_block import BedrockRuntimeGuardrailContentBlock


class BedrockRuntimeApplyGuardrailRequest(BaseModel):
    guardrailIdentifier: StrictStr
    guardrailVersion: StrictStr
    source: Literal['INPUT', 'OUTPUT']
    content: list[BedrockRuntimeGuardrailContentBlock]
    outputScope: Literal['INTERVENTIONS', 'FULL'] | None = None
