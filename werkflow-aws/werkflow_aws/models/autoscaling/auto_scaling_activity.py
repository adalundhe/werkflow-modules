from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class AutoScalingActivity(BaseModel):
    ActivityId: StrictStr | None = None
    AutoScalingGroupName: StrictStr | None = None
    Description: StrictStr | None = None
    Cause: StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    StatusCode: StrictStr | None = None
    StatusMessage: StrictStr | None = None
    Progress: StrictInt | None = None
    Details: StrictStr | None = None
    AutoScalingGroupState: StrictStr | None = None
    AutoScalingGroupARN: StrictStr | None = None
