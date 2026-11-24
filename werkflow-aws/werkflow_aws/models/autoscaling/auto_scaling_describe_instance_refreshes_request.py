from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class AutoScalingDescribeInstanceRefreshesRequest(BaseModel):
    AutoScalingGroupName: StrictStr
    InstanceRefreshIds: list[StrictStr] | None = None
    NextToken: StrictStr | None = None
    MaxRecords: StrictInt | None = None
