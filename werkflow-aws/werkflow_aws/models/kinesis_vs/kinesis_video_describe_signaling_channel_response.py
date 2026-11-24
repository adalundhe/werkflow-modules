from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .kinesis_video_channel_info import KinesisVideoChannelInfo


class KinesisVideoDescribeSignalingChannelResponse(BaseModel):
    ChannelInfo: KinesisVideoChannelInfo | None = None
    ResponseMetadata: dict[str, Any] | None = None
