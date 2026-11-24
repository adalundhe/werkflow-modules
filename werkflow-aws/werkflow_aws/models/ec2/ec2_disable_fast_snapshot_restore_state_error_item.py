from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_disable_fast_snapshot_restore_state_error import EC2DisableFastSnapshotRestoreStateError


class EC2DisableFastSnapshotRestoreStateErrorItem(BaseModel):
    AvailabilityZone: StrictStr | None = None
    AvailabilityZoneId: StrictStr | None = None
    Error: EC2DisableFastSnapshotRestoreStateError | None = None
