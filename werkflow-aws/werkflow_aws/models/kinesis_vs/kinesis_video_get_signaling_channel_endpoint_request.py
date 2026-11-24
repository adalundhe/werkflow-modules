from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kinesis_video_single_master_channel_endpoint_configuration import KinesisVideoSingleMasterChannelEndpointConfiguration


class KinesisVideoGetSignalingChannelEndpointRequest(BaseModel):
    ChannelARN: StrictStr
    SingleMasterChannelEndpointConfiguration: KinesisVideoSingleMasterChannelEndpointConfiguration | None = None
