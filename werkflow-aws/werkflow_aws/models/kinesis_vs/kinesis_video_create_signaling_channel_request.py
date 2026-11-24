from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .kinesis_video_single_master_configuration import KinesisVideoSingleMasterConfiguration
from .kinesis_video_tag import KinesisVideoTag


class KinesisVideoCreateSignalingChannelRequest(BaseModel):
    ChannelName: StrictStr
    ChannelType: Literal['SINGLE_MASTER', 'FULL_MESH'] | None = None
    SingleMasterConfiguration: KinesisVideoSingleMasterConfiguration | None = None
    Tags: list[KinesisVideoTag] | None = None
