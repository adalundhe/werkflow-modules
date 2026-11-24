from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .open_search_serverless_lifecycle_policy_summary import OpenSearchServerlessLifecyclePolicySummary


class OpenSearchServerlessListLifecyclePoliciesResponse(BaseModel):
    lifecyclePolicySummaries: list[OpenSearchServerlessLifecyclePolicySummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
