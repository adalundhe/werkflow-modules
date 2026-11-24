from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class AutoScalingDescribeAutoScalingInstancesRequest(BaseModel):
    InstanceIds: list[StrictStr] | None = None
    IncludeManagedResources: StrictBool | None = None
    MaxRecords: StrictInt | None = None
    NextToken: StrictStr | None = None
