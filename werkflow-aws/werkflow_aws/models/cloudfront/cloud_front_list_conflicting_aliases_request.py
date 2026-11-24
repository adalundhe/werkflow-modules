from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CloudFrontListConflictingAliasesRequest(BaseModel):
    DistributionId: StrictStr
    Alias: StrictStr
    Marker: StrictStr | None = None
    MaxItems: StrictInt | None = None
