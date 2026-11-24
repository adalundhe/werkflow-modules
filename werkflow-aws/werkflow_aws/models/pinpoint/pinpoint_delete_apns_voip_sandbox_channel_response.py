from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .pinpoint_apns_voip_sandbox_channel_response import PinpointAPNSVoipSandboxChannelResponse


class PinpointDeleteApnsVoipSandboxChannelResponse(BaseModel):
    APNSVoipSandboxChannelResponse: PinpointAPNSVoipSandboxChannelResponse | None = None
    ResponseMetadata: dict[str, Any] | None = None
