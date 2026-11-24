from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTDetachPolicyRequest(BaseModel):
    policyName: StrictStr
    target: StrictStr
