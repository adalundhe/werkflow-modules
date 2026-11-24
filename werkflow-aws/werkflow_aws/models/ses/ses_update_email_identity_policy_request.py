from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESUpdateEmailIdentityPolicyRequest(BaseModel):
    EmailIdentity: StrictStr
    PolicyName: StrictStr
    Policy: StrictStr
