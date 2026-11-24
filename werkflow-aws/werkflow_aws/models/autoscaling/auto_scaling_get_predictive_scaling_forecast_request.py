from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class AutoScalingGetPredictiveScalingForecastRequest(BaseModel):
    AutoScalingGroupName: StrictStr
    PolicyName: StrictStr
    StartTime: datetime.datetime | StrictStr
    EndTime: datetime.datetime | StrictStr
