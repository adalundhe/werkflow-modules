from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class KMSRevokeGrantRequest(BaseModel):
    KeyId: StrictStr
    GrantId: StrictStr
    DryRun: StrictBool | None = None
