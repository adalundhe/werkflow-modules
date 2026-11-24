from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .support_trusted_advisor_check_refresh_status import SupportTrustedAdvisorCheckRefreshStatus


class SupportRefreshTrustedAdvisorCheckResponse(BaseModel):
    status: SupportTrustedAdvisorCheckRefreshStatus | None = None
    ResponseMetadata: dict[str, Any] | None = None
