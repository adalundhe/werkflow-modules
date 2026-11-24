from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockRegisterMarketplaceModelEndpointRequest(BaseModel):
    endpointIdentifier: StrictStr
    modelSourceIdentifier: StrictStr
