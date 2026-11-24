from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessAudioExtractionConfiguration(BaseModel):
    audioExtractionStatus: StrictStr | None = None
