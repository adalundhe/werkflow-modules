from __future__ import annotations
from pydantic import BaseModel
from .access_analyzer_analysis_rule_criteria import AccessAnalyzerAnalysisRuleCriteria


class AccessAnalyzerAnalysisRule(BaseModel):
    exclusions: list[AccessAnalyzerAnalysisRuleCriteria] | None = None
