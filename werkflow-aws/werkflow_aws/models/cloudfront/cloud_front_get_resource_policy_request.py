from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontGetResourcePolicyRequest(BaseModel):
    ResourceArn: StrictStr
