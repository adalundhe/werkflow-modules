from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AccessAnalyzerInternalAccessAnalysisRuleCriteria(BaseModel):
    accountIds: list[StrictStr] | None = None
    resourceTypes: list[StrictStr] | None = None
    resourceArns: list[StrictStr] | None = None
