from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class NetworkManagerGetCoreNetworkChangeSetRequest(BaseModel):
    CoreNetworkId: StrictStr
    PolicyVersionId: StrictInt
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
