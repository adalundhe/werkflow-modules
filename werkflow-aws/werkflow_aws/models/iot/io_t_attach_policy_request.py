from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTAttachPolicyRequest(BaseModel):
    policyName: StrictStr
    target: StrictStr
