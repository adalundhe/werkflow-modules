from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2EnableFastSnapshotRestoresRequest(BaseModel):
    SourceSnapshotIds: list[StrictStr]
    AvailabilityZones: list[StrictStr] | None = None
    AvailabilityZoneIds: list[StrictStr] | None = None
    DryRun: StrictBool | None = None
