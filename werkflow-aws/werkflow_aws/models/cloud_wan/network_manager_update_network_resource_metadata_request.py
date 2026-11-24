from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerUpdateNetworkResourceMetadataRequest(BaseModel):
    GlobalNetworkId: StrictStr
    ResourceArn: StrictStr
    Metadata: dict[StrictStr, StrictStr]
