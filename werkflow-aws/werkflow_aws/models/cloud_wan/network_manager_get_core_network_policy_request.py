from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class NetworkManagerGetCoreNetworkPolicyRequest(BaseModel):
    CoreNetworkId: StrictStr
    PolicyVersionId: StrictInt | None = None
    Alias: Literal['LIVE', 'LATEST'] | None = None
