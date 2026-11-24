from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontDistributionResourceId(BaseModel):
    DistributionId: StrictStr | None = None
    DistributionTenantId: StrictStr | None = None
