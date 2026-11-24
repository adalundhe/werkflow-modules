from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .kinesis_video_channel_info import KinesisVideoChannelInfo


class KinesisVideoListSignalingChannelsResponse(BaseModel):
    ChannelInfoList: list[KinesisVideoChannelInfo] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
