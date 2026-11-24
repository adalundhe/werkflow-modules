from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .support_trusted_advisor_check_result import SupportTrustedAdvisorCheckResult


class SupportDescribeTrustedAdvisorCheckResultResponse(BaseModel):
    result: SupportTrustedAdvisorCheckResult | None = None
    ResponseMetadata: dict[str, Any] | None = None
