from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NotificationSchemeNotificationDetailsPayload(BaseModel):
    notificationType: StrictStr | None = None
    parameter: StrictStr | None = None
