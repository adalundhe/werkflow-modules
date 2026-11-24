from __future__ import annotations
from pydantic import BaseModel
from .access_analyzer_internal_access_analysis_rule import AccessAnalyzerInternalAccessAnalysisRule


class AccessAnalyzerInternalAccessConfiguration(BaseModel):
    analysisRule: AccessAnalyzerInternalAccessAnalysisRule | None = None
