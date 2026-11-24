from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontConflictingAlias(BaseModel):
    Alias: StrictStr | None = None
    DistributionId: StrictStr | None = None
    AccountId: StrictStr | None = None
