from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class ConnectCreateNotificationResponse(BaseModel):
    NotificationId: StrictStr | None = None
    NotificationArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
