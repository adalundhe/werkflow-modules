from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_filter_model import EC2FilterModel


class EC2DescribeTrafficMirrorSessionsRequest(BaseModel):
    TrafficMirrorSessionIds: list[StrictStr] | None = None
    DryRun: StrictBool | None = None
    Filters: list[EC2FilterModel] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
