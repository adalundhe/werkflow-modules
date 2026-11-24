from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class NetworkManagerGetLinkAssociationsRequest(BaseModel):
    GlobalNetworkId: StrictStr
    DeviceId: StrictStr | None = None
    LinkId: StrictStr | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
