from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PollyGetVoiceRequest(BaseModel):
    VoiceId: StrictStr
