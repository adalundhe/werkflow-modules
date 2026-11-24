from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bedrock_tag import BedrockTag


class BedrockCreateAutomatedReasoningPolicyVersionRequest(BaseModel):
    policyArn: StrictStr
    lastUpdatedDefinitionHash: StrictStr
    clientRequestToken: StrictStr | None = None
    tags: list[BedrockTag] | None = None
