from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_snapshot_tier_status import EC2SnapshotTierStatus


class EC2DescribeSnapshotTierStatusResponse(BaseModel):
    SnapshotTierStatuses: list[EC2SnapshotTierStatus] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
