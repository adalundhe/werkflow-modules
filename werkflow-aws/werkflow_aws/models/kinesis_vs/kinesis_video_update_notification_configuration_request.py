from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kinesis_video_notification_configuration import KinesisVideoNotificationConfiguration


class KinesisVideoUpdateNotificationConfigurationRequest(BaseModel):
    StreamName: StrictStr | None = None
    StreamARN: StrictStr | None = None
    NotificationConfiguration: KinesisVideoNotificationConfiguration | None = None
