from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightAudioExtractionConfiguration(BaseModel):
    audioExtractionStatus: StrictStr | None = None
