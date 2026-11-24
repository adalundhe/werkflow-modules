from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontListDistributionsByKeyGroupRequest(BaseModel):
    KeyGroupId: StrictStr
    Marker: StrictStr | None = None
    MaxItems: StrictStr | None = None
