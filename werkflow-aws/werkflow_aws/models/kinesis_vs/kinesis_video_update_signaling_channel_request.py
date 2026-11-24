from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kinesis_video_single_master_configuration import KinesisVideoSingleMasterConfiguration


class KinesisVideoUpdateSignalingChannelRequest(BaseModel):
    ChannelARN: StrictStr
    CurrentVersion: StrictStr
    SingleMasterConfiguration: KinesisVideoSingleMasterConfiguration | None = None
