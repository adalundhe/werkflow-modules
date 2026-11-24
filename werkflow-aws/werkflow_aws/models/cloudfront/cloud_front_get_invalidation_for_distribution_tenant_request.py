from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontGetInvalidationForDistributionTenantRequest(BaseModel):
    DistributionTenantId: StrictStr
    Id: StrictStr
