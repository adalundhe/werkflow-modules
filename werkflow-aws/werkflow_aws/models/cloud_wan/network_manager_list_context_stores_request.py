from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class NetworkManagerListContextStoresRequest(BaseModel):
    GlobalNetworkId: StrictStr | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
