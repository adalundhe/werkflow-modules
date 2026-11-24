from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class NetworkManagerGetConnectionsRequest(BaseModel):
    GlobalNetworkId: StrictStr
    ConnectionIds: list[StrictStr] | None = None
    DeviceId: StrictStr | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
