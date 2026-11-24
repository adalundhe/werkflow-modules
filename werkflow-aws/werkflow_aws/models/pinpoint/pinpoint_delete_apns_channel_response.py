from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .pinpoint_apns_channel_response import PinpointAPNSChannelResponse


class PinpointDeleteApnsChannelResponse(BaseModel):
    APNSChannelResponse: PinpointAPNSChannelResponse | None = None
    ResponseMetadata: dict[str, Any] | None = None
