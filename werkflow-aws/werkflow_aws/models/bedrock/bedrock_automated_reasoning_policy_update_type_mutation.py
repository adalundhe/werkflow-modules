from __future__ import annotations
from pydantic import BaseModel
from .bedrock_automated_reasoning_policy_definition_type import BedrockAutomatedReasoningPolicyDefinitionType


class BedrockAutomatedReasoningPolicyUpdateTypeMutation(BaseModel):
    type: BedrockAutomatedReasoningPolicyDefinitionType | None = None
