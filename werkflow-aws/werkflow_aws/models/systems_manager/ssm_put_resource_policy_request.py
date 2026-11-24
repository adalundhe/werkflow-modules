from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMPutResourcePolicyRequest(BaseModel):
    ResourceArn: StrictStr
    Policy: StrictStr
    PolicyId: StrictStr | None = None
    PolicyHash: StrictStr | None = None
