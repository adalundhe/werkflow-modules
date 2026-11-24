from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMSetDefaultPolicyVersionRequest(BaseModel):
    PolicyArn: StrictStr
    VersionId: StrictStr
