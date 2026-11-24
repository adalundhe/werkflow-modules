from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class StorageGatewayListTapePoolsRequest(BaseModel):
    PoolARNs: list[StrictStr] | None = None
    Marker: StrictStr | None = None
    Limit: StrictInt | None = None
