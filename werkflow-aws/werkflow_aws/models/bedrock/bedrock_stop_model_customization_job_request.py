from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockStopModelCustomizationJobRequest(BaseModel):
    jobIdentifier: StrictStr
