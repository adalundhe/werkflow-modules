from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AccessAnalyzerAnalysisRuleCriteria(BaseModel):
    accountIds: list[StrictStr] | None = None
    resourceTags: list[dict[StrictStr, StrictStr]] | None = None
