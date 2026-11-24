from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SNSPutDataProtectionPolicyRequest(BaseModel):
    ResourceArn: StrictStr
    DataProtectionPolicy: StrictStr
