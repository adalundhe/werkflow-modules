from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTDetachPrincipalPolicyRequest(BaseModel):
    policyName: StrictStr
    principal: StrictStr
