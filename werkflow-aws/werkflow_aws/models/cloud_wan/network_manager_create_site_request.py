from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .network_manager_location import NetworkManagerLocation
from .network_manager_tag import NetworkManagerTag


class NetworkManagerCreateSiteRequest(BaseModel):
    GlobalNetworkId: StrictStr
    Description: StrictStr | None = None
    Location: NetworkManagerLocation | None = None
    Tags: list[NetworkManagerTag] | None = None
