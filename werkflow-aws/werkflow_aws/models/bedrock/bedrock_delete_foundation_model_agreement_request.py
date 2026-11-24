from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockDeleteFoundationModelAgreementRequest(BaseModel):
    modelId: StrictStr
