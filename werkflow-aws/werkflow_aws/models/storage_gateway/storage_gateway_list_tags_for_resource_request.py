from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class StorageGatewayListTagsForResourceRequest(BaseModel):
    ResourceARN: StrictStr
    Marker: StrictStr | None = None
    Limit: StrictInt | None = None
