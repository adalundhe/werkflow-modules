from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockGetCustomModelRequest(BaseModel):
    modelIdentifier: StrictStr
