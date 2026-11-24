from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontListDistributionsByAnycastIpListIdRequest(BaseModel):
    AnycastIpListId: StrictStr
    Marker: StrictStr | None = None
    MaxItems: StrictStr | None = None
