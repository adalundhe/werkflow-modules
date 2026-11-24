from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class NetworkManagerDeleteCoreNetworkPolicyVersionRequest(BaseModel):
    CoreNetworkId: StrictStr
    PolicyVersionId: StrictInt
