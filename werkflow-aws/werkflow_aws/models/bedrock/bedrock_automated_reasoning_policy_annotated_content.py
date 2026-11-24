from __future__ import annotations
from pydantic import BaseModel
from .bedrock_automated_reasoning_policy_annotated_line import BedrockAutomatedReasoningPolicyAnnotatedLine


class BedrockAutomatedReasoningPolicyAnnotatedContent(BaseModel):
    line: BedrockAutomatedReasoningPolicyAnnotatedLine | None = None
