from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kinesis_video_deletion_config import KinesisVideoDeletionConfig
from .kinesis_video_recorder_config import KinesisVideoRecorderConfig
from .kinesis_video_uploader_config import KinesisVideoUploaderConfig


class KinesisVideoEdgeConfig(BaseModel):
    HubDeviceArn: StrictStr | None = None
    RecorderConfig: KinesisVideoRecorderConfig | None = None
    UploaderConfig: KinesisVideoUploaderConfig | None = None
    DeletionConfig: KinesisVideoDeletionConfig | None = None
