from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_describe_fast_snapshot_restore_success_item import EC2DescribeFastSnapshotRestoreSuccessItem


class EC2DescribeFastSnapshotRestoresResponse(BaseModel):
    FastSnapshotRestores: list[EC2DescribeFastSnapshotRestoreSuccessItem] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
