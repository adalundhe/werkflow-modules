from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSDisassociateAccessPolicyRequest(BaseModel):
    clusterName: StrictStr
    principalArn: StrictStr
    policyArn: StrictStr
