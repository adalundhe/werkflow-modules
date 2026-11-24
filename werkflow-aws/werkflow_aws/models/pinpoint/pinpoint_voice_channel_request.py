from __future__ import annotations
from pydantic import BaseModel, StrictBool


class PinpointVoiceChannelRequest(BaseModel):
    Enabled: StrictBool | None = None
