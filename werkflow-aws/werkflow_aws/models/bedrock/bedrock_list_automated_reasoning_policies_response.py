from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .bedrock_automated_reasoning_policy_summary import BedrockAutomatedReasoningPolicySummary


class BedrockListAutomatedReasoningPoliciesResponse(BaseModel):
    automatedReasoningPolicySummaries: list[BedrockAutomatedReasoningPolicySummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
