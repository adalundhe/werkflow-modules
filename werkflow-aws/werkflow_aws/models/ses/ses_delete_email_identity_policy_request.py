from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESDeleteEmailIdentityPolicyRequest(BaseModel):
    EmailIdentity: StrictStr
    PolicyName: StrictStr
