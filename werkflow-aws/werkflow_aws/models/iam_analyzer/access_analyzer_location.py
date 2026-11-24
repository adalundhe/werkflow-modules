from __future__ import annotations
from pydantic import BaseModel
from .access_analyzer_path_element import AccessAnalyzerPathElement
from .access_analyzer_span import AccessAnalyzerSpan


class AccessAnalyzerLocation(BaseModel):
    path: list[AccessAnalyzerPathElement] | None = None
    span: AccessAnalyzerSpan | None = None
