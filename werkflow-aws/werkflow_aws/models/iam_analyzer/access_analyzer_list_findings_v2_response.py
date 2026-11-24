from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .access_analyzer_finding_summary_v2 import AccessAnalyzerFindingSummaryV2


class AccessAnalyzerListFindingsV2Response(BaseModel):
    findings: list[AccessAnalyzerFindingSummaryV2] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
