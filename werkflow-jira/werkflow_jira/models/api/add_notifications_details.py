from __future__ import annotations
from pydantic import BaseModel, ConfigDict
from .notification_scheme_event_details import NotificationSchemeEventDetails


class AddNotificationsDetails(BaseModel):
    model_config = ConfigDict(extra="allow")

    notificationSchemeEvents: list[NotificationSchemeEventDetails] | None = None
