from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .bedrock_guardrail_summary import BedrockGuardrailSummary


class BedrockListGuardrailsResponse(BaseModel):
    guardrails: list[BedrockGuardrailSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
