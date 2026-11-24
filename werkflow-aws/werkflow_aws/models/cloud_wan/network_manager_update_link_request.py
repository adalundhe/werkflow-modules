from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .network_manager_bandwidth import NetworkManagerBandwidth


class NetworkManagerUpdateLinkRequest(BaseModel):
    GlobalNetworkId: StrictStr
    LinkId: StrictStr
    Description: StrictStr | None = None
    Type: StrictStr | None = None
    Bandwidth: NetworkManagerBandwidth | None = None
    Provider: StrictStr | None = None
