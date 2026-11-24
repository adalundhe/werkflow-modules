from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kinesis_video_stream_storage_configuration import KinesisVideoStreamStorageConfiguration


class KinesisVideoUpdateStreamStorageConfigurationRequest(BaseModel):
    CurrentVersion: StrictStr
    StreamStorageConfiguration: KinesisVideoStreamStorageConfiguration
    StreamName: StrictStr | None = None
    StreamARN: StrictStr | None = None
