from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class SecurityHubAwsRdsDbClusterMember(BaseModel):
    IsClusterWriter: StrictBool | None = None
    PromotionTier: StrictInt | None = None
    DbInstanceIdentifier: StrictStr | None = None
    DbClusterParameterGroupStatus: StrictStr | None = None
