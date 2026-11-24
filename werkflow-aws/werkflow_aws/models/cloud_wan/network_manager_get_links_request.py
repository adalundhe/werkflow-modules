from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class NetworkManagerGetLinksRequest(BaseModel):
    GlobalNetworkId: StrictStr
    LinkIds: list[StrictStr] | None = None
    SiteId: StrictStr | None = None
    Type: StrictStr | None = None
    Provider: StrictStr | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
