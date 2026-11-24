from __future__ import annotations
from pydantic import BaseModel, StrictInt


class CodeGuruMetrics(BaseModel):
    MeteredLinesOfCodeCount: StrictInt | None = None
    SuppressedLinesOfCodeCount: StrictInt | None = None
    FindingsCount: StrictInt | None = None
