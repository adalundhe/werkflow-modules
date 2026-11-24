from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontGetCachePolicyRequest(BaseModel):
    Id: StrictStr
