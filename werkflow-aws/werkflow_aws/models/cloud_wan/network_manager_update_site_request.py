from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .network_manager_location import NetworkManagerLocation


class NetworkManagerUpdateSiteRequest(BaseModel):
    GlobalNetworkId: StrictStr
    SiteId: StrictStr
    Description: StrictStr | None = None
    Location: NetworkManagerLocation | None = None
