from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightDeletePolicyAssignmentRequest(BaseModel):
    AccountId: StrictStr
    PolicyArn: StrictStr
    PrincipalArn: StrictStr
    Revision: StrictInt | None = None
