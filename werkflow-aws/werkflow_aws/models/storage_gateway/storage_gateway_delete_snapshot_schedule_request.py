from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StorageGatewayDeleteSnapshotScheduleRequest(BaseModel):
    VolumeARN: StrictStr
