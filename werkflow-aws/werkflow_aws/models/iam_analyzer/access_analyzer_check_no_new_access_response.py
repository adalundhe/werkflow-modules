from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .access_analyzer_reason_summary import AccessAnalyzerReasonSummary


class AccessAnalyzerCheckNoNewAccessResponse(BaseModel):
    result: StrictStr | None = None
    message: StrictStr | None = None
    reasons: list[AccessAnalyzerReasonSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
