from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexVoiceSettings(BaseModel):
    engine: StrictStr | None = None
    voiceId: StrictStr | None = None
