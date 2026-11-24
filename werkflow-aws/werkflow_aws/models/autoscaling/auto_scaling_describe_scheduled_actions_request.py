from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class AutoScalingDescribeScheduledActionsRequest(BaseModel):
    AutoScalingGroupName: StrictStr | None = None
    ScheduledActionNames: list[StrictStr] | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    IncludeManagedResources: StrictBool | None = None
    NextToken: StrictStr | None = None
    MaxRecords: StrictInt | None = None
