from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kinesis_video_notification_destination_config import KinesisVideoNotificationDestinationConfig


class KinesisVideoNotificationConfiguration(BaseModel):
    Status: StrictStr | None = None
    DestinationConfig: KinesisVideoNotificationDestinationConfig | None = None
