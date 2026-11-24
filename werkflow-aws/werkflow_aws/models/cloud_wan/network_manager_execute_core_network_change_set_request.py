from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class NetworkManagerExecuteCoreNetworkChangeSetRequest(BaseModel):
    CoreNetworkId: StrictStr
    PolicyVersionId: StrictInt
