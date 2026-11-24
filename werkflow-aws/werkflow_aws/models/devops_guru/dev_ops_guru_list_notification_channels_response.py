from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .dev_ops_guru_notification_channel import DevOpsGuruNotificationChannel


class DevOpsGuruListNotificationChannelsResponse(BaseModel):
    Channels: list[DevOpsGuruNotificationChannel] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
