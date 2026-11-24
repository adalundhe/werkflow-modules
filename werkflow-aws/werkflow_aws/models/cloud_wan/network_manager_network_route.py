from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .network_manager_network_route_destination import NetworkManagerNetworkRouteDestination


class NetworkManagerNetworkRoute(BaseModel):
    DestinationCidrBlock: StrictStr | None = None
    Destinations: list[NetworkManagerNetworkRouteDestination] | None = None
    PrefixListId: StrictStr | None = None
    State: StrictStr | None = None
    Type: StrictStr | None = None
