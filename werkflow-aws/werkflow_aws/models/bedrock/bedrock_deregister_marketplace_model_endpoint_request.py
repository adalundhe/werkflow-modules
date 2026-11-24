from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockDeregisterMarketplaceModelEndpointRequest(BaseModel):
    endpointArn: StrictStr
