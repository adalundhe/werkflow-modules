from __future__ import annotations
from pydantic import BaseModel
from .access_analyzer_internal_access_analysis_rule_criteria import AccessAnalyzerInternalAccessAnalysisRuleCriteria


class AccessAnalyzerInternalAccessAnalysisRule(BaseModel):
    inclusions: list[AccessAnalyzerInternalAccessAnalysisRuleCriteria] | None = None
