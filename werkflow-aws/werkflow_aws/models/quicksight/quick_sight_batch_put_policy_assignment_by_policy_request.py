from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_put_assignment_entry import QuickSightPutAssignmentEntry


class QuickSightBatchPutPolicyAssignmentByPolicyRequest(BaseModel):
    AccountId: StrictStr
    PolicyArn: StrictStr
    Assignments: list[QuickSightPutAssignmentEntry]
