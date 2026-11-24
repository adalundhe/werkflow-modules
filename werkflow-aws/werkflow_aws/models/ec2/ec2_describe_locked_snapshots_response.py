from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_locked_snapshots_info import EC2LockedSnapshotsInfo


class EC2DescribeLockedSnapshotsResponse(BaseModel):
    Snapshots: list[EC2LockedSnapshotsInfo] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
