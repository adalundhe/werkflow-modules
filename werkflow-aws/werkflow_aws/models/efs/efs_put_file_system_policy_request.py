from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EFSPutFileSystemPolicyRequest(BaseModel):
    FileSystemId: StrictStr
    Policy: StrictStr
    BypassPolicyLockoutSafetyCheck: StrictBool | None = None
