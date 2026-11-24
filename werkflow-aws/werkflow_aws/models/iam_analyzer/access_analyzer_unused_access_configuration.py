from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .access_analyzer_analysis_rule import AccessAnalyzerAnalysisRule


class AccessAnalyzerUnusedAccessConfiguration(BaseModel):
    unusedAccessAge: StrictInt | None = None
    analysisRule: AccessAnalyzerAnalysisRule | None = None
