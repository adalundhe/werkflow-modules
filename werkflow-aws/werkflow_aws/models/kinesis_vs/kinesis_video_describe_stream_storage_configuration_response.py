from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .kinesis_video_stream_storage_configuration import KinesisVideoStreamStorageConfiguration


class KinesisVideoDescribeStreamStorageConfigurationResponse(BaseModel):
    StreamName: StrictStr | None = None
    StreamARN: StrictStr | None = None
    StreamStorageConfiguration: KinesisVideoStreamStorageConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
