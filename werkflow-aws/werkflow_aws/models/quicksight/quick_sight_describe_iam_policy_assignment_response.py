from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_iam_policy_assignment import QuickSightIAMPolicyAssignment


class QuickSightDescribeIAMPolicyAssignmentResponse(BaseModel):
    IAMPolicyAssignment: QuickSightIAMPolicyAssignment | None = None
    RequestId: StrictStr | None = None
    Status: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
