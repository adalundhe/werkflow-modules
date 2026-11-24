from __future__ import annotations
from pydantic import BaseModel
from .dev_ops_guru_notification_channel_config import DevOpsGuruNotificationChannelConfig


class DevOpsGuruAddNotificationChannelRequest(BaseModel):
    Config: DevOpsGuruNotificationChannelConfig
