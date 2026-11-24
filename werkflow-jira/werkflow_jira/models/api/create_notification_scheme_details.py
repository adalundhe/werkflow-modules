from __future__ import annotations
from pydantic import BaseModel, ConfigDict, StrictStr
from .notification_scheme_event_details import NotificationSchemeEventDetails


class CreateNotificationSchemeDetails(BaseModel):
    model_config = ConfigDict(extra="allow")

    description: StrictStr | None = None
    name: StrictStr | None = None
    notificationSchemeEvents: list[NotificationSchemeEventDetails] | None = None
