from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .access_analyzer_analyzed_resource_summary import AccessAnalyzerAnalyzedResourceSummary


class AccessAnalyzerListAnalyzedResourcesResponse(BaseModel):
    analyzedResources: list[AccessAnalyzerAnalyzedResourceSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
