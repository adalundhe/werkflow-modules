from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .auto_scaling_filter import AutoScalingFilter


class AutoScalingDescribeTagsRequest(BaseModel):
    Filters: list[AutoScalingFilter] | None = None
    IncludeManagedResources: StrictBool | None = None
    NextToken: StrictStr | None = None
    MaxRecords: StrictInt | None = None
