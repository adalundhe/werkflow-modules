from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_filter import EC2Filter


class EC2DescribeSecurityGroupsRequest(BaseModel):
    GroupIds: list[StrictStr] | None = None
    GroupNames: list[StrictStr] | None = None
    Filters: list[EC2Filter] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    DryRun: StrictBool | None = None
