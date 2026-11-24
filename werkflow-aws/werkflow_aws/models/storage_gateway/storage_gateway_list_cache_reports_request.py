from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StorageGatewayListCacheReportsRequest(BaseModel):
    Marker: StrictStr | None = None
