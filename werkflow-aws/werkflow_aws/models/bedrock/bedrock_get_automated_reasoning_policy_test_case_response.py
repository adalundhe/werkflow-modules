from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .bedrock_automated_reasoning_policy_test_case import BedrockAutomatedReasoningPolicyTestCase


class BedrockGetAutomatedReasoningPolicyTestCaseResponse(BaseModel):
    policyArn: StrictStr | None = None
    testCase: BedrockAutomatedReasoningPolicyTestCase | None = None
    ResponseMetadata: dict[str, Any] | None = None
