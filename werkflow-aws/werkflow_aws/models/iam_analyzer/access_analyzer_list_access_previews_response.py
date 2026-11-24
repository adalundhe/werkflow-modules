from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .access_analyzer_access_preview_summary import AccessAnalyzerAccessPreviewSummary


class AccessAnalyzerListAccessPreviewsResponse(BaseModel):
    accessPreviews: list[AccessAnalyzerAccessPreviewSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
