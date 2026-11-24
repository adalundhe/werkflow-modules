from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontListDistributionsByWebACLIdRequest(BaseModel):
    WebACLId: StrictStr
    Marker: StrictStr | None = None
    MaxItems: StrictStr | None = None
