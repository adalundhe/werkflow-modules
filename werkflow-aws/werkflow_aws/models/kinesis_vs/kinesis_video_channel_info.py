from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .kinesis_video_single_master_configuration import KinesisVideoSingleMasterConfiguration


class KinesisVideoChannelInfo(BaseModel):
    ChannelName: StrictStr | None = None
    ChannelARN: StrictStr | None = None
    ChannelType: StrictStr | None = None
    ChannelStatus: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    SingleMasterConfiguration: KinesisVideoSingleMasterConfiguration | None = None
    Version: StrictStr | None = None
