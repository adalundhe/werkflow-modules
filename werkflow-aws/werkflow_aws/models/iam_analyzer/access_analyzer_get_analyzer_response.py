from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .access_analyzer_analyzer_summary import AccessAnalyzerAnalyzerSummary


class AccessAnalyzerGetAnalyzerResponse(BaseModel):
    analyzer: AccessAnalyzerAnalyzerSummary | None = None
    ResponseMetadata: dict[str, Any] | None = None
