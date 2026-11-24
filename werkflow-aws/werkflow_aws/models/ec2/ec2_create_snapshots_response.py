from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_snapshot_info import EC2SnapshotInfo


class EC2CreateSnapshotsResponse(BaseModel):
    Snapshots: list[EC2SnapshotInfo] | None = None
    ResponseMetadata: dict[str, Any] | None = None
