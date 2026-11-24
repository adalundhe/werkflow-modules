from __future__ import annotations
from pydantic import BaseModel, StrictInt


class AccessAnalyzerSubstring(BaseModel):
    start: StrictInt | None = None
    length: StrictInt | None = None
