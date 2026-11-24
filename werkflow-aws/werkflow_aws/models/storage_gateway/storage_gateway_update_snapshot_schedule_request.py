from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .storage_gateway_tag import StorageGatewayTag


class StorageGatewayUpdateSnapshotScheduleRequest(BaseModel):
    VolumeARN: StrictStr
    StartAt: StrictInt
    RecurrenceInHours: StrictInt
    Description: StrictStr | None = None
    Tags: list[StorageGatewayTag] | None = None
