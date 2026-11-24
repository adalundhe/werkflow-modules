from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTSetDefaultPolicyVersionRequest(BaseModel):
    policyName: StrictStr
    policyVersionId: StrictStr
