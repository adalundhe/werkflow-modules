from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .access_analyzer_criterion import AccessAnalyzerCriterion


class AccessAnalyzerUpdateArchiveRuleRequest(BaseModel):
    analyzerName: StrictStr
    ruleName: StrictStr
    filter: dict[StrictStr, AccessAnalyzerCriterion]
    clientToken: StrictStr | None = None
