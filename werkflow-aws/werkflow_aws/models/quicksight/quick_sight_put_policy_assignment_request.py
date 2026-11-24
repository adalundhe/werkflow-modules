from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightPutPolicyAssignmentRequest(BaseModel):
    AccountId: StrictStr
    PolicyArn: StrictStr
    PrincipalArn: StrictStr
    ExistingPolicyArn: StrictStr | None = None
    Revision: StrictInt | None = None
