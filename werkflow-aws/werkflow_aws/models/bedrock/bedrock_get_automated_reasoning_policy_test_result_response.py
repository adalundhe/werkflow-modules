from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .bedrock_automated_reasoning_policy_test_result import BedrockAutomatedReasoningPolicyTestResult


class BedrockGetAutomatedReasoningPolicyTestResultResponse(BaseModel):
    testResult: BedrockAutomatedReasoningPolicyTestResult | None = None
    ResponseMetadata: dict[str, Any] | None = None
