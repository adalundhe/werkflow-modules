from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudTrailPutResourcePolicyRequest(BaseModel):
    ResourceArn: StrictStr
    ResourcePolicy: StrictStr
