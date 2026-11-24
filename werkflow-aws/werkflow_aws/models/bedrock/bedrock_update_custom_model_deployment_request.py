from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockUpdateCustomModelDeploymentRequest(BaseModel):
    modelArn: StrictStr
    customModelDeploymentIdentifier: StrictStr
