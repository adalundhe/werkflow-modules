from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .kinesis_video_stream_info import KinesisVideoStreamInfo


class KinesisVideoDescribeStreamResponse(BaseModel):
    StreamInfo: KinesisVideoStreamInfo | None = None
    ResponseMetadata: dict[str, Any] | None = None
