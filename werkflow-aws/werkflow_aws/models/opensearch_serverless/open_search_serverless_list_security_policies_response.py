from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .open_search_serverless_security_policy_summary import OpenSearchServerlessSecurityPolicySummary


class OpenSearchServerlessListSecurityPoliciesResponse(BaseModel):
    securityPolicySummaries: list[OpenSearchServerlessSecurityPolicySummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
