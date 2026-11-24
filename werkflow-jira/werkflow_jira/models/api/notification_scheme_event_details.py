from __future__ import annotations
from pydantic import BaseModel, ConfigDict
from .notification_scheme_event_type_id import NotificationSchemeEventTypeId
from .notification_scheme_notification_details import NotificationSchemeNotificationDetails


class NotificationSchemeEventDetails(BaseModel):
    model_config = ConfigDict(extra="allow")

    event: NotificationSchemeEventTypeId | None = None
    notifications: list[NotificationSchemeNotificationDetails] | None = None
