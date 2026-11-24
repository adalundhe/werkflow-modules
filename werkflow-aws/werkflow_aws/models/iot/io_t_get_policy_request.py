from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTGetPolicyRequest(BaseModel):
    policyName: StrictStr
