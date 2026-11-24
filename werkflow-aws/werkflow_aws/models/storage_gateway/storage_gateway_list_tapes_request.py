from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class StorageGatewayListTapesRequest(BaseModel):
    TapeARNs: list[StrictStr] | None = None
    Marker: StrictStr | None = None
    Limit: StrictInt | None = None
