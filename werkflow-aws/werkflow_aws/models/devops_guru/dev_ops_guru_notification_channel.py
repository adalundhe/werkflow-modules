from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dev_ops_guru_notification_channel_config import DevOpsGuruNotificationChannelConfig


class DevOpsGuruNotificationChannel(BaseModel):
    Id: StrictStr | None = None
    Config: DevOpsGuruNotificationChannelConfig | None = None
