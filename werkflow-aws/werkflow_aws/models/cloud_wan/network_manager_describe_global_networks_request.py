from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class NetworkManagerDescribeGlobalNetworksRequest(BaseModel):
    GlobalNetworkIds: list[StrictStr] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
