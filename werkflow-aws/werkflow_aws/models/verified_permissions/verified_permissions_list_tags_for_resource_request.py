from __future__ import annotations
from pydantic import BaseModel, StrictStr


class VerifiedPermissionsListTagsForResourceRequest(BaseModel):
    resourceArn: StrictStr
