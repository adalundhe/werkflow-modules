from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontListDistributionsByResponseHeadersPolicyIdRequest(BaseModel):
    ResponseHeadersPolicyId: StrictStr
    Marker: StrictStr | None = None
    MaxItems: StrictStr | None = None
