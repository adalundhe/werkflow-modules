from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockDeleteImportedModelRequest(BaseModel):
    modelIdentifier: StrictStr
