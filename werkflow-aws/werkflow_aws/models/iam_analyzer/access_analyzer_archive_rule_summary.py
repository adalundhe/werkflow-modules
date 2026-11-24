from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .access_analyzer_criterion import AccessAnalyzerCriterion


class AccessAnalyzerArchiveRuleSummary(BaseModel):
    ruleName: StrictStr | None = None
    filter: dict[StrictStr, AccessAnalyzerCriterion] | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
