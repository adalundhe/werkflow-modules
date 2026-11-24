from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockDeleteMarketplaceModelEndpointRequest(BaseModel):
    endpointArn: StrictStr
