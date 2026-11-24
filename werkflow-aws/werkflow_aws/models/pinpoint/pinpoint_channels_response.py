from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_channel_response import PinpointChannelResponse


class PinpointChannelsResponse(BaseModel):
    Channels: dict[StrictStr, PinpointChannelResponse] | None = None
