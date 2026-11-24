from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .open_search_serverless_access_policy_summary import OpenSearchServerlessAccessPolicySummary


class OpenSearchServerlessListAccessPoliciesResponse(BaseModel):
    accessPolicySummaries: list[OpenSearchServerlessAccessPolicySummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
