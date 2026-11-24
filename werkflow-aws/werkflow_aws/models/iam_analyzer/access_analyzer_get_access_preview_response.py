from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .access_analyzer_access_preview import AccessAnalyzerAccessPreview


class AccessAnalyzerGetAccessPreviewResponse(BaseModel):
    accessPreview: AccessAnalyzerAccessPreview | None = None
    ResponseMetadata: dict[str, Any] | None = None
