from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ec2_filter_model import EC2FilterModel


class EC2DescribeHostsRequest(BaseModel):
    HostIds: list[StrictStr] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    Filter: list[EC2FilterModel] | None = None
