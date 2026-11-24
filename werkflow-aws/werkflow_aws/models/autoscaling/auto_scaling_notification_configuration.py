from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AutoScalingNotificationConfiguration(BaseModel):
    AutoScalingGroupName: StrictStr | None = None
    TopicARN: StrictStr | None = None
    NotificationType: StrictStr | None = None
