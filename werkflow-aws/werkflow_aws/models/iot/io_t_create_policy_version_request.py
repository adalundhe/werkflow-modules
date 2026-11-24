from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class IoTCreatePolicyVersionRequest(BaseModel):
    policyName: StrictStr
    policyDocument: StrictStr
    setAsDefault: StrictBool | None = None
