from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockDeleteProvisionedModelThroughputRequest(BaseModel):
    provisionedModelId: StrictStr
