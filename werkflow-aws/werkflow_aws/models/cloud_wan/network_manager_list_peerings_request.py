from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class NetworkManagerListPeeringsRequest(BaseModel):
    CoreNetworkId: StrictStr | None = None
    PeeringType: Literal['TRANSIT_GATEWAY'] | None = None
    EdgeLocation: StrictStr | None = None
    State: Literal['CREATING', 'FAILED', 'AVAILABLE', 'DELETING'] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
