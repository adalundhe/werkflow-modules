from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_notification_search_summary import ConnectNotificationSearchSummary


class ConnectSearchNotificationsResponse(BaseModel):
    Notifications: list[ConnectNotificationSearchSummary] | None = None
    NextToken: StrictStr | None = None
    ApproximateTotalCount: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
