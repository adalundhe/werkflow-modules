from __future__ import annotations
from pydantic import BaseModel, StrictInt


class AccessAnalyzerInternalAccessResourceTypeDetails(BaseModel):
    totalActiveFindings: StrictInt | None = None
    totalResolvedFindings: StrictInt | None = None
    totalArchivedFindings: StrictInt | None = None
