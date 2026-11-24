from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_disable_fast_snapshot_restore_state_error_item import EC2DisableFastSnapshotRestoreStateErrorItem


class EC2DisableFastSnapshotRestoreErrorItem(BaseModel):
    SnapshotId: StrictStr | None = None
    FastSnapshotRestoreStateErrors: list[EC2DisableFastSnapshotRestoreStateErrorItem] | None = None
