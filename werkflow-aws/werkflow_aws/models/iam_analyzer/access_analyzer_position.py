from __future__ import annotations
from pydantic import BaseModel, StrictInt


class AccessAnalyzerPosition(BaseModel):
    line: StrictInt | None = None
    column: StrictInt | None = None
    offset: StrictInt | None = None
