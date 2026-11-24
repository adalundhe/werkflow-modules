from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .access_analyzer_finding import AccessAnalyzerFinding


class AccessAnalyzerGetFindingResponse(BaseModel):
    finding: AccessAnalyzerFinding | None = None
    ResponseMetadata: dict[str, Any] | None = None
