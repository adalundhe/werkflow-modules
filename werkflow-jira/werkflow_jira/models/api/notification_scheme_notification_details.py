from __future__ import annotations
from pydantic import BaseModel, ConfigDict, StrictStr


class NotificationSchemeNotificationDetails(BaseModel):
    model_config = ConfigDict(extra="allow")

    notificationType: StrictStr | None = None
    parameter: StrictStr | None = None
