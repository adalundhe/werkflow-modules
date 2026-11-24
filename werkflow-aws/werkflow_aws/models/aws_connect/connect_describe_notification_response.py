from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .connect_notification import ConnectNotification


class ConnectDescribeNotificationResponse(BaseModel):
    Notification: ConnectNotification | None = None
    ResponseMetadata: dict[str, Any] | None = None
