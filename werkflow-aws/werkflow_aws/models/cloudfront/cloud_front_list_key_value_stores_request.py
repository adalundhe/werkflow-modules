from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontListKeyValueStoresRequest(BaseModel):
    Marker: StrictStr | None = None
    MaxItems: StrictStr | None = None
    Status: StrictStr | None = None
