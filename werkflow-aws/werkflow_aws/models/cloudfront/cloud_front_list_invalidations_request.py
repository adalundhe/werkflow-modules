from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontListInvalidationsRequest(BaseModel):
    DistributionId: StrictStr
    Marker: StrictStr | None = None
    MaxItems: StrictStr | None = None
