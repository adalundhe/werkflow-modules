from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisVideoDescribeMediaStorageConfigurationRequest(BaseModel):
    ChannelName: StrictStr | None = None
    ChannelARN: StrictStr | None = None
