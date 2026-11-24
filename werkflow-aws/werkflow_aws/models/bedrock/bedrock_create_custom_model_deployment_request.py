from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bedrock_tag import BedrockTag


class BedrockCreateCustomModelDeploymentRequest(BaseModel):
    modelDeploymentName: StrictStr
    modelArn: StrictStr
    description: StrictStr | None = None
    tags: list[BedrockTag] | None = None
    clientRequestToken: StrictStr | None = None
