from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class KMSListResourceTagsRequest(BaseModel):
    KeyId: StrictStr
    Limit: StrictInt | None = None
    Marker: StrictStr | None = None
