from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .bedrock_automated_reasoning_policy_annotated_content import BedrockAutomatedReasoningPolicyAnnotatedContent


class BedrockAutomatedReasoningPolicyAnnotatedChunk(BaseModel):
    pageNumber: StrictInt | None = None
    content: list[BedrockAutomatedReasoningPolicyAnnotatedContent] | None = None
