from __future__ import annotations
from pydantic import BaseModel, StrictStr


class VerifiedPermissionsUntagResourceRequest(BaseModel):
    resourceArn: StrictStr
    tagKeys: list[StrictStr]
