from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightActiveIAMPolicyAssignment(BaseModel):
    AssignmentName: StrictStr | None = None
    PolicyArn: StrictStr | None = None
