from __future__ import annotations
from pydantic import BaseModel
from .event_notification import EventNotification
from .notification_event import NotificationEvent


class NotificationSchemeEvent(BaseModel):
    event: NotificationEvent | None = None
    notifications: list[EventNotification] | None = None
