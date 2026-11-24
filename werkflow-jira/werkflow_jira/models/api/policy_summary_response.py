from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .policy_summary import PolicySummary


class PolicySummaryResponse(BaseModel):
    isLast: StrictBool | None = None
    maxResults: StrictInt | None = None
    nextPageCursor: StrictStr | None = None
    startAt: StrictInt | None = None
    total: StrictInt | None = None
    values: list[PolicySummary] | None = None
