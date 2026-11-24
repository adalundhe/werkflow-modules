from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockGetCustomModelDeploymentRequest(BaseModel):
    customModelDeploymentIdentifier: StrictStr
