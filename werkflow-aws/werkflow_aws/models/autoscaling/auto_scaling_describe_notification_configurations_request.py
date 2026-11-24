from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class AutoScalingDescribeNotificationConfigurationsRequest(BaseModel):
    AutoScalingGroupNames: list[StrictStr] | None = None
    IncludeManagedResources: StrictBool | None = None
    NextToken: StrictStr | None = None
    MaxRecords: StrictInt | None = None
