from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockCreateFoundationModelAgreementRequest(BaseModel):
    offerToken: StrictStr
    modelId: StrictStr
