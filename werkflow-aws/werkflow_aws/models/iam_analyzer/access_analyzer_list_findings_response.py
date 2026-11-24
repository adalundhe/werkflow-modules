from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .access_analyzer_finding_summary import AccessAnalyzerFindingSummary


class AccessAnalyzerListFindingsResponse(BaseModel):
    findings: list[AccessAnalyzerFindingSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
