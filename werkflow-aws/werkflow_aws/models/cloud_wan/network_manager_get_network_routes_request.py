from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .network_manager_route_table_identifier import NetworkManagerRouteTableIdentifier


class NetworkManagerGetNetworkRoutesRequest(BaseModel):
    GlobalNetworkId: StrictStr
    RouteTableIdentifier: NetworkManagerRouteTableIdentifier
    ExactCidrMatches: list[StrictStr] | None = None
    LongestPrefixMatches: list[StrictStr] | None = None
    SubnetOfMatches: list[StrictStr] | None = None
    SupernetOfMatches: list[StrictStr] | None = None
    PrefixListIds: list[StrictStr] | None = None
    States: list[Literal['ACTIVE', 'BLACKHOLE']] | None = None
    Types: list[Literal['PROPAGATED', 'STATIC', 'SYSTEM']] | None = None
    DestinationFilters: dict[StrictStr, list[StrictStr]] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
