from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDescribeNotificationRequest(BaseModel):
    InstanceId: StrictStr
    NotificationId: StrictStr
