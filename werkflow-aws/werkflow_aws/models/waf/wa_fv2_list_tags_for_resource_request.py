from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class WAFv2ListTagsForResourceRequest(BaseModel):
    ResourceARN: StrictStr
    NextMarker: StrictStr | None = None
    Limit: StrictInt | None = None
