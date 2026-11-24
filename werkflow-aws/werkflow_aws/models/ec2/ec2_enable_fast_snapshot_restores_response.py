from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_enable_fast_snapshot_restore_error_item import EC2EnableFastSnapshotRestoreErrorItem
from .ec2_enable_fast_snapshot_restore_success_item import EC2EnableFastSnapshotRestoreSuccessItem


class EC2EnableFastSnapshotRestoresResponse(BaseModel):
    Successful: list[EC2EnableFastSnapshotRestoreSuccessItem] | None = None
    Unsuccessful: list[EC2EnableFastSnapshotRestoreErrorItem] | None = None
    ResponseMetadata: dict[str, Any] | None = None
