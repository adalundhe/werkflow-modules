from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontListDistributionsByOwnedResourceRequest(BaseModel):
    ResourceArn: StrictStr
    Marker: StrictStr | None = None
    MaxItems: StrictStr | None = None
