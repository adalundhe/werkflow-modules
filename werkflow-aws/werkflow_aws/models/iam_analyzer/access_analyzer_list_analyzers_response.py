from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .access_analyzer_analyzer_summary import AccessAnalyzerAnalyzerSummary


class AccessAnalyzerListAnalyzersResponse(BaseModel):
    analyzers: list[AccessAnalyzerAnalyzerSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
