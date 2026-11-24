from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CloudFrontListInvalidationsForDistributionTenantRequest(BaseModel):
    Id: StrictStr
    Marker: StrictStr | None = None
    MaxItems: StrictInt | None = None
