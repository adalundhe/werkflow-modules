from __future__ import annotations
from pydantic import BaseModel, StrictStr


class VerifiedPermissionsTagResourceRequest(BaseModel):
    resourceArn: StrictStr
    tags: dict[StrictStr, StrictStr]
