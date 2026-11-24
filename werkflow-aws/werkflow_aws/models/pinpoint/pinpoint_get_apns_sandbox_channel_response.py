from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .pinpoint_apns_sandbox_channel_response import PinpointAPNSSandboxChannelResponse


class PinpointGetApnsSandboxChannelResponse(BaseModel):
    APNSSandboxChannelResponse: PinpointAPNSSandboxChannelResponse | None = None
    ResponseMetadata: dict[str, Any] | None = None
