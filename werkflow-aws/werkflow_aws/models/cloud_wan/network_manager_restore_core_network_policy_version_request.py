from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class NetworkManagerRestoreCoreNetworkPolicyVersionRequest(BaseModel):
    CoreNetworkId: StrictStr
    PolicyVersionId: StrictInt
