from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class BedrockListFoundationModelAgreementOffersRequest(BaseModel):
    modelId: StrictStr
    offerType: Literal['ALL', 'PUBLIC'] | None = None
