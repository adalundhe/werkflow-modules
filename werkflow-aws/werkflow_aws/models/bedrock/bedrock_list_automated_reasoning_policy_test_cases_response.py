from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .bedrock_automated_reasoning_policy_test_case import BedrockAutomatedReasoningPolicyTestCase


class BedrockListAutomatedReasoningPolicyTestCasesResponse(BaseModel):
    testCases: list[BedrockAutomatedReasoningPolicyTestCase] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
