from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_enable_fast_snapshot_restore_state_error_item import EC2EnableFastSnapshotRestoreStateErrorItem


class EC2EnableFastSnapshotRestoreErrorItem(BaseModel):
    SnapshotId: StrictStr | None = None
    FastSnapshotRestoreStateErrors: list[EC2EnableFastSnapshotRestoreStateErrorItem] | None = None
