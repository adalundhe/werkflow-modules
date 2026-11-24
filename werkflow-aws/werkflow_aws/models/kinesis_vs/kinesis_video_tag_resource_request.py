from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kinesis_video_tag import KinesisVideoTag


class KinesisVideoTagResourceRequest(BaseModel):
    ResourceARN: StrictStr
    Tags: list[KinesisVideoTag]
