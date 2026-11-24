from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_voice_channel_request import PinpointVoiceChannelRequest


class PinpointUpdateVoiceChannelRequest(BaseModel):
    ApplicationId: StrictStr
    VoiceChannelRequest: PinpointVoiceChannelRequest
