from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .eks_access_scope import EKSAccessScope


class EKSAssociateAccessPolicyRequest(BaseModel):
    clusterName: StrictStr
    principalArn: StrictStr
    policyArn: StrictStr
    accessScope: EKSAccessScope
