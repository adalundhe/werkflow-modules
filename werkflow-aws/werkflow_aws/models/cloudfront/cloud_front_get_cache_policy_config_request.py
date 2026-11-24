from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontGetCachePolicyConfigRequest(BaseModel):
    Id: StrictStr
