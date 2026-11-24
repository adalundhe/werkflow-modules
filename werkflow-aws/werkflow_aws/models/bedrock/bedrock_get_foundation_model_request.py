from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockGetFoundationModelRequest(BaseModel):
    modelIdentifier: StrictStr
    projectIdentifier: StrictStr | None = None
