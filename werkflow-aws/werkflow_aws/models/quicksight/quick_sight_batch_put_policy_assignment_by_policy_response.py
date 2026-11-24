from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .quick_sight_batch_put_policy_assignment_error import QuickSightBatchPutPolicyAssignmentError
from .quick_sight_batch_put_policy_assignment_success import QuickSightBatchPutPolicyAssignmentSuccess


class QuickSightBatchPutPolicyAssignmentByPolicyResponse(BaseModel):
    PolicyArn: StrictStr | None = None
    Success: list[QuickSightBatchPutPolicyAssignmentSuccess] | None = None
    Errors: list[QuickSightBatchPutPolicyAssignmentError] | None = None
    ResponseMetadata: dict[str, Any] | None = None
