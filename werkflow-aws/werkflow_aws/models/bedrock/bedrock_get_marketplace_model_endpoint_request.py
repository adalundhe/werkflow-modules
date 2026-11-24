from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockGetMarketplaceModelEndpointRequest(BaseModel):
    endpointArn: StrictStr
