from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .storage_gateway_tag import StorageGatewayTag


class StorageGatewayDescribeSnapshotScheduleResponse(BaseModel):
    VolumeARN: StrictStr | None = None
    StartAt: StrictInt | None = None
    RecurrenceInHours: StrictInt | None = None
    Description: StrictStr | None = None
    Timezone: StrictStr | None = None
    Tags: list[StorageGatewayTag] | None = None
    ResponseMetadata: dict[str, Any] | None = None
