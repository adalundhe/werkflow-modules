from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudTrailDeleteResourcePolicyRequest(BaseModel):
    ResourceArn: StrictStr
