from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .pinpoint_channels_response import PinpointChannelsResponse


class PinpointGetChannelsResponse(BaseModel):
    ChannelsResponse: PinpointChannelsResponse | None = None
    ResponseMetadata: dict[str, Any] | None = None
