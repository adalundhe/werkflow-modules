from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StorageGatewayListVolumeRecoveryPointsRequest(BaseModel):
    GatewayARN: StrictStr
