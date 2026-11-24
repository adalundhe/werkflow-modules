from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PollyDeleteVoiceRequest(BaseModel):
    VoiceId: StrictStr
