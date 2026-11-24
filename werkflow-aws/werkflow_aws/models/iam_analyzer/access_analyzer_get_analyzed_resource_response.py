from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .access_analyzer_analyzed_resource import AccessAnalyzerAnalyzedResource


class AccessAnalyzerGetAnalyzedResourceResponse(BaseModel):
    resource: AccessAnalyzerAnalyzedResource | None = None
    ResponseMetadata: dict[str, Any] | None = None
