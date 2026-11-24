from __future__ import annotations
from pydantic import BaseModel
from .dev_ops_guru_notification_filter_config import DevOpsGuruNotificationFilterConfig
from .dev_ops_guru_sns_channel_config import DevOpsGuruSnsChannelConfig


class DevOpsGuruNotificationChannelConfig(BaseModel):
    Sns: DevOpsGuruSnsChannelConfig | None = None
    Filters: DevOpsGuruNotificationFilterConfig | None = None
