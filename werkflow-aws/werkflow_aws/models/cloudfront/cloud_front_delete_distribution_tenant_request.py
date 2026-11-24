from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontDeleteDistributionTenantRequest(BaseModel):
    Id: StrictStr
    IfMatch: StrictStr
