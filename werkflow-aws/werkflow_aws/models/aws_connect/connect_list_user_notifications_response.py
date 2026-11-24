from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_user_notification_summary import ConnectUserNotificationSummary


class ConnectListUserNotificationsResponse(BaseModel):
    UserNotifications: list[ConnectUserNotificationSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
