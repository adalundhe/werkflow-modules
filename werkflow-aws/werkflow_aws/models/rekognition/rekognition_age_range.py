from __future__ import annotations
from pydantic import BaseModel, StrictInt


class RekognitionAgeRange(BaseModel):
    Low: StrictInt | None = None
    High: StrictInt | None = None
