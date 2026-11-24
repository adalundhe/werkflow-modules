from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_snapshot import EC2Snapshot


class EC2DescribeSnapshotsResponse(BaseModel):
    Snapshots: list[EC2Snapshot] | None = None
    NextToken: StrictStr | None = None
