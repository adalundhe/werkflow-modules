from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDeleteNotificationRequest(BaseModel):
    InstanceId: StrictStr
    NotificationId: StrictStr
