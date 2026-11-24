from __future__ import annotations
from pydantic import BaseModel
from .access_analyzer_position import AccessAnalyzerPosition


class AccessAnalyzerSpan(BaseModel):
    start: AccessAnalyzerPosition | None = None
    end: AccessAnalyzerPosition | None = None
