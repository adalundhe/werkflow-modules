from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .kinesis_video_media_storage_configuration import KinesisVideoMediaStorageConfiguration


class KinesisVideoDescribeMediaStorageConfigurationResponse(BaseModel):
    MediaStorageConfiguration: KinesisVideoMediaStorageConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
