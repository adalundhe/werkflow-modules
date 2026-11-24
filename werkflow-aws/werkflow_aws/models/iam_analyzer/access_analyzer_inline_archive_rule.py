from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .access_analyzer_criterion import AccessAnalyzerCriterion


class AccessAnalyzerInlineArchiveRule(BaseModel):
    ruleName: StrictStr
    filter: dict[StrictStr, AccessAnalyzerCriterion]
