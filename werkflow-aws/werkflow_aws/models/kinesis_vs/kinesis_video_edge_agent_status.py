from __future__ import annotations
from pydantic import BaseModel
from .kinesis_video_last_recorder_status import KinesisVideoLastRecorderStatus
from .kinesis_video_last_uploader_status import KinesisVideoLastUploaderStatus


class KinesisVideoEdgeAgentStatus(BaseModel):
    LastRecorderStatus: KinesisVideoLastRecorderStatus | None = None
    LastUploaderStatus: KinesisVideoLastUploaderStatus | None = None
