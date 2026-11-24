from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudHSMPutResourcePolicyRequest(BaseModel):
    ResourceArn: StrictStr | None = None
    Policy: StrictStr | None = None
