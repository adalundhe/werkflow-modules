from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .kinesis_video_notification_configuration import KinesisVideoNotificationConfiguration


class KinesisVideoDescribeNotificationConfigurationResponse(BaseModel):
    NotificationConfiguration: KinesisVideoNotificationConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
