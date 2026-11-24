from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_notification import ConnectNotification


class ConnectListNotificationsResponse(BaseModel):
    NextToken: StrictStr | None = None
    NotificationSummaryList: list[ConnectNotification] | None = None
    ResponseMetadata: dict[str, Any] | None = None
