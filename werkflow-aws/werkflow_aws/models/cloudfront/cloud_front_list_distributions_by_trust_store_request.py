from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontListDistributionsByTrustStoreRequest(BaseModel):
    TrustStoreIdentifier: StrictStr
    Marker: StrictStr | None = None
    MaxItems: StrictStr | None = None
