from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StorageGatewayUpdateGatewaySoftwareNowRequest(BaseModel):
    GatewayARN: StrictStr
