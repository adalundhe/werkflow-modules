from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class StorageGatewayListFileSharesRequest(BaseModel):
    GatewayARN: StrictStr | None = None
    Limit: StrictInt | None = None
    Marker: StrictStr | None = None
