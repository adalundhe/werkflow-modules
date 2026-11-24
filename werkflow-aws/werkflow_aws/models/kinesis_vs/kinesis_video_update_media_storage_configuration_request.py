from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kinesis_video_media_storage_configuration import KinesisVideoMediaStorageConfiguration


class KinesisVideoUpdateMediaStorageConfigurationRequest(BaseModel):
    ChannelARN: StrictStr
    MediaStorageConfiguration: KinesisVideoMediaStorageConfiguration
