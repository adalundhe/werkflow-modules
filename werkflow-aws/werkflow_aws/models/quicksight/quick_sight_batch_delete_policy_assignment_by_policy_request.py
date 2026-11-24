from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightBatchDeletePolicyAssignmentByPolicyRequest(BaseModel):
    AccountId: StrictStr
    PolicyArn: StrictStr
    PrincipalArns: list[StrictStr]
