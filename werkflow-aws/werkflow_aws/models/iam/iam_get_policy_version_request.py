from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMGetPolicyVersionRequest(BaseModel):
    PolicyArn: StrictStr
    VersionId: StrictStr
