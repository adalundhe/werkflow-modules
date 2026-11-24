from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_disable_fast_snapshot_restore_error_item import EC2DisableFastSnapshotRestoreErrorItem
from .ec2_disable_fast_snapshot_restore_success_item import EC2DisableFastSnapshotRestoreSuccessItem


class EC2DisableFastSnapshotRestoresResponse(BaseModel):
    Successful: list[EC2DisableFastSnapshotRestoreSuccessItem] | None = None
    Unsuccessful: list[EC2DisableFastSnapshotRestoreErrorItem] | None = None
    ResponseMetadata: dict[str, Any] | None = None
