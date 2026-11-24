from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESCreateEmailIdentityPolicyRequest(BaseModel):
    EmailIdentity: StrictStr
    PolicyName: StrictStr
    Policy: StrictStr
