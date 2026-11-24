from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StorageGatewayListVolumeInitiatorsRequest(BaseModel):
    VolumeARN: StrictStr
