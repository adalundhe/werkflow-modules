from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .support_trusted_advisor_check_description import SupportTrustedAdvisorCheckDescription


class SupportDescribeTrustedAdvisorChecksResponse(BaseModel):
    checks: list[SupportTrustedAdvisorCheckDescription] | None = None
    ResponseMetadata: dict[str, Any] | None = None
