from __future__ import annotations
from pydantic import BaseModel
from .kinesis_video_media_source_config import KinesisVideoMediaSourceConfig
from .kinesis_video_schedule_config import KinesisVideoScheduleConfig


class KinesisVideoRecorderConfig(BaseModel):
    MediaSourceConfig: KinesisVideoMediaSourceConfig | None = None
    ScheduleConfig: KinesisVideoScheduleConfig | None = None
