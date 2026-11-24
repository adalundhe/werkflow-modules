from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class NetworkManagerGetDevicesRequest(BaseModel):
    GlobalNetworkId: StrictStr
    DeviceIds: list[StrictStr] | None = None
    SiteId: StrictStr | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
