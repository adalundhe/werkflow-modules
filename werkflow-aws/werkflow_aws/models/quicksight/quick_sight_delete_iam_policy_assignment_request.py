from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDeleteIAMPolicyAssignmentRequest(BaseModel):
    AwsAccountId: StrictStr
    AssignmentName: StrictStr
    Namespace: StrictStr
