from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StorageGatewayDeleteVolumeRequest(BaseModel):
    VolumeARN: StrictStr
