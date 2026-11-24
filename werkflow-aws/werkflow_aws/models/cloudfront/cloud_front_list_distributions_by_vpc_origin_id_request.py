from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontListDistributionsByVpcOriginIdRequest(BaseModel):
    VpcOriginId: StrictStr
    Marker: StrictStr | None = None
    MaxItems: StrictStr | None = None
