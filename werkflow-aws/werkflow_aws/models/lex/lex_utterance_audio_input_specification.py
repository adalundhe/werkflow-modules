from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexUtteranceAudioInputSpecification(BaseModel):
    audioFileS3Location: StrictStr | None = None
