from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDescribeApprovalPolicyRequest(BaseModel):
    PolicyId: StrictStr
