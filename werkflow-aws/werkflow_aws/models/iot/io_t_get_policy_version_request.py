from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTGetPolicyVersionRequest(BaseModel):
    policyName: StrictStr
    policyVersionId: StrictStr
