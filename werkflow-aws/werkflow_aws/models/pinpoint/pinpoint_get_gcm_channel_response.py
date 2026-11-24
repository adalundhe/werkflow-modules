from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .pinpoint_gcm_channel_response import PinpointGCMChannelResponse


class PinpointGetGcmChannelResponse(BaseModel):
    GCMChannelResponse: PinpointGCMChannelResponse | None = None
    ResponseMetadata: dict[str, Any] | None = None
