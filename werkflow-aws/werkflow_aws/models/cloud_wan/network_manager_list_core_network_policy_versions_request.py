from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class NetworkManagerListCoreNetworkPolicyVersionsRequest(BaseModel):
    CoreNetworkId: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
