from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class AutoScalingDescribeTrafficSourcesRequest(BaseModel):
    AutoScalingGroupName: StrictStr
    TrafficSourceType: StrictStr | None = None
    NextToken: StrictStr | None = None
    MaxRecords: StrictInt | None = None
