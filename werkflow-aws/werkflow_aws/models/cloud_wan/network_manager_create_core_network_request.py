from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .network_manager_tag import NetworkManagerTag


class NetworkManagerCreateCoreNetworkRequest(BaseModel):
    GlobalNetworkId: StrictStr
    Description: StrictStr | None = None
    Tags: list[NetworkManagerTag] | None = None
    PolicyDocument: StrictStr | None = None
    ClientToken: StrictStr | None = None
