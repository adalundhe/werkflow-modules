from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisVideoDescribeSignalingChannelRequest(BaseModel):
    ChannelName: StrictStr | None = None
    ChannelARN: StrictStr | None = None
