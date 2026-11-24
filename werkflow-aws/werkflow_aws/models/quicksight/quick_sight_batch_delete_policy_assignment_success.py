from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightBatchDeletePolicyAssignmentSuccess(BaseModel):
    PrincipalArn: StrictStr | None = None
