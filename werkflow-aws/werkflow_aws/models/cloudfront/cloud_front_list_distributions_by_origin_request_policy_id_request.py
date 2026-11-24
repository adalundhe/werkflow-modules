from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontListDistributionsByOriginRequestPolicyIdRequest(BaseModel):
    OriginRequestPolicyId: StrictStr
    Marker: StrictStr | None = None
    MaxItems: StrictStr | None = None
