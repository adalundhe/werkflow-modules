from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .auto_scaling_filter import AutoScalingFilter


class AutoScalingDescribeScalingActivitiesRequest(BaseModel):
    ActivityIds: list[StrictStr] | None = None
    AutoScalingGroupName: StrictStr | None = None
    IncludeDeletedGroups: StrictBool | None = None
    IncludeManagedResources: StrictBool | None = None
    MaxRecords: StrictInt | None = None
    NextToken: StrictStr | None = None
    Filters: list[AutoScalingFilter] | None = None
