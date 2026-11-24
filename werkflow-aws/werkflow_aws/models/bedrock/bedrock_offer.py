from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bedrock_term_details import BedrockTermDetails


class BedrockOffer(BaseModel):
    offerId: StrictStr | None = None
    offerToken: StrictStr | None = None
    termDetails: BedrockTermDetails | None = None
