from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .bedrock_automated_reasoning_policy_definition import BedrockAutomatedReasoningPolicyDefinition


class BedrockExportAutomatedReasoningPolicyVersionResponse(BaseModel):
    policyDefinition: BedrockAutomatedReasoningPolicyDefinition | None = None
    ResponseMetadata: dict[str, Any] | None = None
