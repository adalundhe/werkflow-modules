from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisVideoDeleteSignalingChannelRequest(BaseModel):
    ChannelARN: StrictStr
    CurrentVersion: StrictStr | None = None
