from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .quick_sight_batch_delete_policy_assignment_error import QuickSightBatchDeletePolicyAssignmentError
from .quick_sight_batch_delete_policy_assignment_success import QuickSightBatchDeletePolicyAssignmentSuccess


class QuickSightBatchDeletePolicyAssignmentByPolicyResponse(BaseModel):
    PolicyArn: StrictStr | None = None
    Success: list[QuickSightBatchDeletePolicyAssignmentSuccess] | None = None
    Errors: list[QuickSightBatchDeletePolicyAssignmentError] | None = None
    ResponseMetadata: dict[str, Any] | None = None
