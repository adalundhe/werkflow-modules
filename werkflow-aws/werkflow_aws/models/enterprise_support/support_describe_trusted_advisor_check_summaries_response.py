from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .support_trusted_advisor_check_summary import SupportTrustedAdvisorCheckSummary


class SupportDescribeTrustedAdvisorCheckSummariesResponse(BaseModel):
    summaries: list[SupportTrustedAdvisorCheckSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
