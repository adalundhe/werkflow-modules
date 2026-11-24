from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockGetImportedModelRequest(BaseModel):
    modelIdentifier: StrictStr
