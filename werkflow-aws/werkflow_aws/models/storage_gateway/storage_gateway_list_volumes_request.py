from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class StorageGatewayListVolumesRequest(BaseModel):
    GatewayARN: StrictStr | None = None
    Marker: StrictStr | None = None
    Limit: StrictInt | None = None
