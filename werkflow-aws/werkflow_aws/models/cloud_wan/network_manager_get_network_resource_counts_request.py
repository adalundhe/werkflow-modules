from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class NetworkManagerGetNetworkResourceCountsRequest(BaseModel):
    GlobalNetworkId: StrictStr
    ResourceType: StrictStr | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
