from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class AutoScalingDescribeWarmPoolRequest(BaseModel):
    AutoScalingGroupName: StrictStr
    MaxRecords: StrictInt | None = None
    NextToken: StrictStr | None = None
