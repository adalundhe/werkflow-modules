from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontGetOriginRequestPolicyConfigRequest(BaseModel):
    Id: StrictStr
