from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDeleteApprovalPolicyRequest(BaseModel):
    PolicyId: StrictStr
