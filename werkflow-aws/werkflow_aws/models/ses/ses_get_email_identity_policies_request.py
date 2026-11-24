from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESGetEmailIdentityPoliciesRequest(BaseModel):
    EmailIdentity: StrictStr
