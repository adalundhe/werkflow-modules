from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTAttachPrincipalPolicyRequest(BaseModel):
    policyName: StrictStr
    principal: StrictStr
