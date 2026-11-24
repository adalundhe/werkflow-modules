from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTDeletePolicyVersionRequest(BaseModel):
    policyName: StrictStr
    policyVersionId: StrictStr
