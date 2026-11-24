from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .support_trusted_advisor_check_refresh_status import SupportTrustedAdvisorCheckRefreshStatus


class SupportDescribeTrustedAdvisorCheckRefreshStatusesResponse(BaseModel):
    statuses: list[SupportTrustedAdvisorCheckRefreshStatus] | None = None
    ResponseMetadata: dict[str, Any] | None = None
