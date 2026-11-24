from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TranscribeToxicityDetectionSettings(BaseModel):
    ToxicityCategories: list[StrictStr] | None = None
