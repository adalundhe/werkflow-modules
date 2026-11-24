from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightIAMPolicyAssignmentSummary(BaseModel):
    AssignmentName: StrictStr | None = None
    AssignmentStatus: StrictStr | None = None
