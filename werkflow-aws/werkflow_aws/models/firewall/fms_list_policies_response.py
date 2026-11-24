from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .fms_policy_summary import FMSPolicySummary


class FMSListPoliciesResponse(BaseModel):
    PolicyList: list[FMSPolicySummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
