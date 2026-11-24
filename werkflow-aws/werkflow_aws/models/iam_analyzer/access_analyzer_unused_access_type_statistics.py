from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class AccessAnalyzerUnusedAccessTypeStatistics(BaseModel):
    unusedAccessType: StrictStr | None = None
    total: StrictInt | None = None
