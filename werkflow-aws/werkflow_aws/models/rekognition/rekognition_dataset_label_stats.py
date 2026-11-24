from __future__ import annotations
from pydantic import BaseModel, StrictInt


class RekognitionDatasetLabelStats(BaseModel):
    EntryCount: StrictInt | None = None
    BoundingBoxCount: StrictInt | None = None
