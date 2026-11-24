from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .network_manager_bandwidth import NetworkManagerBandwidth
from .network_manager_tag import NetworkManagerTag


class NetworkManagerLink(BaseModel):
    LinkId: StrictStr | None = None
    LinkArn: StrictStr | None = None
    GlobalNetworkId: StrictStr | None = None
    SiteId: StrictStr | None = None
    Description: StrictStr | None = None
    Type: StrictStr | None = None
    Bandwidth: NetworkManagerBandwidth | None = None
    Provider: StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    State: StrictStr | None = None
    Tags: list[NetworkManagerTag] | None = None
