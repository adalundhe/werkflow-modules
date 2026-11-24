from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontDistributionTenantAssociationFilter(BaseModel):
    DistributionId: StrictStr | None = None
    ConnectionGroupId: StrictStr | None = None
