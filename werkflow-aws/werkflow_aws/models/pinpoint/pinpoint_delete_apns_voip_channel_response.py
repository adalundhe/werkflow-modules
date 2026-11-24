from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .pinpoint_apns_voip_channel_response import PinpointAPNSVoipChannelResponse


class PinpointDeleteApnsVoipChannelResponse(BaseModel):
    APNSVoipChannelResponse: PinpointAPNSVoipChannelResponse | None = None
    ResponseMetadata: dict[str, Any] | None = None
