from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .bedrock_automated_reasoning_policy_test_result import BedrockAutomatedReasoningPolicyTestResult


class BedrockListAutomatedReasoningPolicyTestResultsResponse(BaseModel):
    testResults: list[BedrockAutomatedReasoningPolicyTestResult] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
