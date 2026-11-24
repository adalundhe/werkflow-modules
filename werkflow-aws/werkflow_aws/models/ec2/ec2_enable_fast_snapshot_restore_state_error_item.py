from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_enable_fast_snapshot_restore_state_error import EC2EnableFastSnapshotRestoreStateError


class EC2EnableFastSnapshotRestoreStateErrorItem(BaseModel):
    AvailabilityZone: StrictStr | None = None
    AvailabilityZoneId: StrictStr | None = None
    Error: EC2EnableFastSnapshotRestoreStateError | None = None
