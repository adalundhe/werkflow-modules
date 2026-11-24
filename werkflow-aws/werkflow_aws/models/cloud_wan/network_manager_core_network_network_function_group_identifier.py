from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerCoreNetworkNetworkFunctionGroupIdentifier(BaseModel):
    CoreNetworkId: StrictStr | None = None
    NetworkFunctionGroupName: StrictStr | None = None
    EdgeLocation: StrictStr | None = None
