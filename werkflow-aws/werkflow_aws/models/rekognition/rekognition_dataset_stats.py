from __future__ import annotations
from pydantic import BaseModel, StrictInt


class RekognitionDatasetStats(BaseModel):
    LabeledEntries: StrictInt | None = None
    TotalEntries: StrictInt | None = None
    TotalLabels: StrictInt | None = None
    ErrorEntries: StrictInt | None = None
