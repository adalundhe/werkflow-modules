from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontDistributionIdOwner(BaseModel):
    DistributionId: StrictStr | None = None
    OwnerAccountId: StrictStr | None = None
