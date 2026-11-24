from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .notification_scheme_event import NotificationSchemeEvent
from .scope import Scope


class NotificationScheme(BaseModel):
    description: StrictStr | None = None
    expand: StrictStr | None = None
    id: StrictInt | None = None
    name: StrictStr | None = None
    notificationSchemeEvents: list[NotificationSchemeEvent] | None = None
    projects: list[StrictInt] | None = None
    scope: Scope | None = None
    self: StrictStr | None = None
