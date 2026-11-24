from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AutoScalingPutNotificationConfigurationRequest(BaseModel):
    AutoScalingGroupName: StrictStr
    TopicARN: StrictStr
    NotificationTypes: list[StrictStr]
