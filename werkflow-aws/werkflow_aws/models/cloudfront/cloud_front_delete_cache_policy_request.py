from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontDeleteCachePolicyRequest(BaseModel):
    Id: StrictStr
    IfMatch: StrictStr | None = None
