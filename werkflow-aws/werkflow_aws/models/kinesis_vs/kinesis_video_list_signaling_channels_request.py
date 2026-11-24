from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .kinesis_video_channel_name_condition import KinesisVideoChannelNameCondition


class KinesisVideoListSignalingChannelsRequest(BaseModel):
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    ChannelNameCondition: KinesisVideoChannelNameCondition | None = None
