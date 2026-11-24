from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockGetModelCustomizationJobRequest(BaseModel):
    jobIdentifier: StrictStr
