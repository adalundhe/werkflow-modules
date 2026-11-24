from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_snapshot_recycle_bin_info import EC2SnapshotRecycleBinInfo


class EC2ListSnapshotsInRecycleBinResponse(BaseModel):
    Snapshots: list[EC2SnapshotRecycleBinInfo] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
