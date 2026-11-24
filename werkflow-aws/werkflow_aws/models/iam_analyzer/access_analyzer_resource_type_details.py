from __future__ import annotations
from pydantic import BaseModel, StrictInt


class AccessAnalyzerResourceTypeDetails(BaseModel):
    totalActivePublic: StrictInt | None = None
    totalActiveCrossAccount: StrictInt | None = None
    totalActiveErrors: StrictInt | None = None
