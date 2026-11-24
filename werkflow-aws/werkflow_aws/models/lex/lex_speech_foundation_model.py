from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexSpeechFoundationModel(BaseModel):
    modelArn: StrictStr | None = None
    voiceId: StrictStr | None = None
