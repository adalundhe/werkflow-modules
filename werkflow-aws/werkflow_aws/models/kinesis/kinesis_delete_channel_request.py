from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisDeleteChannelRequest(BaseModel):
    ChannelARN: StrictStr
