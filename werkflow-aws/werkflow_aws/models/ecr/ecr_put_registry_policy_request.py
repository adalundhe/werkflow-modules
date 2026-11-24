from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECRPutRegistryPolicyRequest(BaseModel):
    policyText: StrictStr
