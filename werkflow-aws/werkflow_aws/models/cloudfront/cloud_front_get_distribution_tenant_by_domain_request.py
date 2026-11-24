from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontGetDistributionTenantByDomainRequest(BaseModel):
    Domain: StrictStr
