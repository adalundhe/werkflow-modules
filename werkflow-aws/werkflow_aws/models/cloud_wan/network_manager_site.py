from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .network_manager_location import NetworkManagerLocation
from .network_manager_tag import NetworkManagerTag


class NetworkManagerSite(BaseModel):
    SiteId: StrictStr | None = None
    SiteArn: StrictStr | None = None
    GlobalNetworkId: StrictStr | None = None
    Description: StrictStr | None = None
    Location: NetworkManagerLocation | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    State: StrictStr | None = None
    Tags: list[NetworkManagerTag] | None = None
