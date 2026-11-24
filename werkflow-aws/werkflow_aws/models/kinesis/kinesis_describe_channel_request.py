from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisDescribeChannelRequest(BaseModel):
    ChannelARN: StrictStr
