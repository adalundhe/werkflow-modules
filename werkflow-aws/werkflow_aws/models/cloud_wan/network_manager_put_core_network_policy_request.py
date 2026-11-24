from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class NetworkManagerPutCoreNetworkPolicyRequest(BaseModel):
    CoreNetworkId: StrictStr
    PolicyDocument: StrictStr
    Description: StrictStr | None = None
    LatestVersionId: StrictInt | None = None
    ClientToken: StrictStr | None = None
