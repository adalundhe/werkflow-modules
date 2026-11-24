from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .pinpoint_voice_channel_response import PinpointVoiceChannelResponse


class PinpointGetVoiceChannelResponse(BaseModel):
    VoiceChannelResponse: PinpointVoiceChannelResponse | None = None
    ResponseMetadata: dict[str, Any] | None = None
