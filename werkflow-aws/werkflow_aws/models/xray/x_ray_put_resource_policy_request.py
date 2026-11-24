from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class XRayPutResourcePolicyRequest(BaseModel):
    PolicyName: StrictStr
    PolicyDocument: StrictStr
    PolicyRevisionId: StrictStr | None = None
    BypassPolicyLockoutCheck: StrictBool | None = None
