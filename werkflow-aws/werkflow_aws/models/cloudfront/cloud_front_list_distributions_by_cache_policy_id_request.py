from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontListDistributionsByCachePolicyIdRequest(BaseModel):
    CachePolicyId: StrictStr
    Marker: StrictStr | None = None
    MaxItems: StrictStr | None = None
