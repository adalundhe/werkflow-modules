from __future__ import annotations
from pydantic import BaseModel
from .bedrock_automated_reasoning_policy_generated_test_case import BedrockAutomatedReasoningPolicyGeneratedTestCase


class BedrockAutomatedReasoningPolicyGeneratedTestCases(BaseModel):
    generatedTestCases: list[BedrockAutomatedReasoningPolicyGeneratedTestCase] | None = None
