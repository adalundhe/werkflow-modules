from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bedrock_automated_reasoning_policy_definition import BedrockAutomatedReasoningPolicyDefinition
from .bedrock_tag import BedrockTag


class BedrockCreateAutomatedReasoningPolicyRequest(BaseModel):
    name: StrictStr
    description: StrictStr | None = None
    clientRequestToken: StrictStr | None = None
    policyDefinition: BedrockAutomatedReasoningPolicyDefinition | None = None
    kmsKeyId: StrictStr | None = None
    tags: list[BedrockTag] | None = None
