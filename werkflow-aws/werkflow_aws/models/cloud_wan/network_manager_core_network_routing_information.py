from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .network_manager_routing_information_next_hop import NetworkManagerRoutingInformationNextHop


class NetworkManagerCoreNetworkRoutingInformation(BaseModel):
    Prefix: StrictStr | None = None
    NextHop: NetworkManagerRoutingInformationNextHop | None = None
    LocalPreference: StrictStr | None = None
    Med: StrictStr | None = None
    AsPath: list[StrictStr] | None = None
    Communities: list[StrictStr] | None = None
