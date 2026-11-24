from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StorageGatewayDescribeSnapshotScheduleRequest(BaseModel):
    VolumeARN: StrictStr
