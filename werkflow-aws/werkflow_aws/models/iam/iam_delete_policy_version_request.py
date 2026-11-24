from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMDeletePolicyVersionRequest(BaseModel):
    PolicyArn: StrictStr
    VersionId: StrictStr
