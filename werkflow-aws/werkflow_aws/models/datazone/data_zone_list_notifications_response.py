from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_zone_notification_output import DataZoneNotificationOutput


class DataZoneListNotificationsResponse(BaseModel):
    notifications: list[DataZoneNotificationOutput] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
