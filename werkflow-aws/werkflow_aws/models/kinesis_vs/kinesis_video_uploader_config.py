from __future__ import annotations
from pydantic import BaseModel
from .kinesis_video_schedule_config import KinesisVideoScheduleConfig


class KinesisVideoUploaderConfig(BaseModel):
    ScheduleConfig: KinesisVideoScheduleConfig | None = None
