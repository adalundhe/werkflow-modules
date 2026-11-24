from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .network_manager_bandwidth import NetworkManagerBandwidth
from .network_manager_tag import NetworkManagerTag


class NetworkManagerCreateLinkRequest(BaseModel):
    GlobalNetworkId: StrictStr
    Bandwidth: NetworkManagerBandwidth
    SiteId: StrictStr
    Description: StrictStr | None = None
    Type: StrictStr | None = None
    Provider: StrictStr | None = None
    Tags: list[NetworkManagerTag] | None = None
