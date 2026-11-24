from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class KMSPutKeyPolicyRequest(BaseModel):
    KeyId: StrictStr
    Policy: StrictStr
    PolicyName: StrictStr | None = None
    BypassPolicyLockoutSafetyCheck: StrictBool | None = None
