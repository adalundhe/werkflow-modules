from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class QuickSightGetPolicyAssignmentRequest(BaseModel):
    AccountId: StrictStr
    PolicyType: Literal['LIMITS_PROFILE', 'CUSTOM_PERMISSIONS']
    PrincipalArn: StrictStr
