from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockGetFoundationModelAvailabilityRequest(BaseModel):
    modelId: StrictStr
