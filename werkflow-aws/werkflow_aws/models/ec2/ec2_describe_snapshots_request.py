from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_filter import EC2Filter


class EC2DescribeSnapshotsRequest(BaseModel):
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    OwnerIds: list[StrictStr] | None = None
    RestorableByUserIds: list[StrictStr] | None = None
    SnapshotIds: list[StrictStr] | None = None
    Filters: list[EC2Filter] | None = None
    DryRun: StrictBool | None = None
