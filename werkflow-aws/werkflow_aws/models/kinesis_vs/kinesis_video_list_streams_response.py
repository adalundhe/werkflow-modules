from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .kinesis_video_stream_info import KinesisVideoStreamInfo


class KinesisVideoListStreamsResponse(BaseModel):
    StreamInfoList: list[KinesisVideoStreamInfo] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
