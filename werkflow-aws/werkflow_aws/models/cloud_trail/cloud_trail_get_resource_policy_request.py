from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudTrailGetResourcePolicyRequest(BaseModel):
    ResourceArn: StrictStr
