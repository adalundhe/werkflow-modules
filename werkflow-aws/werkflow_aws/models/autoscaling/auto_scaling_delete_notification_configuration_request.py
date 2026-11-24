from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AutoScalingDeleteNotificationConfigurationRequest(BaseModel):
    AutoScalingGroupName: StrictStr
    TopicARN: StrictStr
