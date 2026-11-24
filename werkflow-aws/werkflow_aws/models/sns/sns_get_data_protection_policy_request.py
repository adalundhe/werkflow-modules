from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SNSGetDataProtectionPolicyRequest(BaseModel):
    ResourceArn: StrictStr
