from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt
from .kinesis_video_local_size_config import KinesisVideoLocalSizeConfig


class KinesisVideoDeletionConfig(BaseModel):
    EdgeRetentionInHours: StrictInt | None = None
    LocalSizeConfig: KinesisVideoLocalSizeConfig | None = None
    DeleteAfterUpload: StrictBool | None = None
