from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMNotificationConfig(BaseModel):
    NotificationArn: StrictStr | None = None
    NotificationEvents: list[StrictStr] | None = None
    NotificationType: StrictStr | None = None
