from __future__ import annotations
from pydantic import BaseModel
from .notification_scheme_event_id_payload import NotificationSchemeEventIDPayload
from .notification_scheme_notification_details_payload import NotificationSchemeNotificationDetailsPayload


class NotificationSchemeEventPayload(BaseModel):
    event: NotificationSchemeEventIDPayload | None = None
    notifications: list[NotificationSchemeNotificationDetailsPayload] | None = None
