from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .quick_sight_approval_policy import QuickSightApprovalPolicy


class QuickSightListApprovalPoliciesResponse(BaseModel):
    Policies: list[QuickSightApprovalPolicy] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
