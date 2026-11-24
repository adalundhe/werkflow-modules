from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CloudFrontListTrustStoresRequest(BaseModel):
    Marker: StrictStr | None = None
    MaxItems: StrictInt | None = None
