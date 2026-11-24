from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .network_manager_core_network_network_function_group_identifier import NetworkManagerCoreNetworkNetworkFunctionGroupIdentifier
from .network_manager_core_network_segment_edge_identifier import NetworkManagerCoreNetworkSegmentEdgeIdentifier
from .network_manager_network_route import NetworkManagerNetworkRoute


class NetworkManagerGetNetworkRoutesResponse(BaseModel):
    RouteTableArn: StrictStr | None = None
    CoreNetworkSegmentEdge: NetworkManagerCoreNetworkSegmentEdgeIdentifier | None = None
    CoreNetworkNetworkFunctionGroup: NetworkManagerCoreNetworkNetworkFunctionGroupIdentifier | None = None
    RouteTableType: StrictStr | None = None
    RouteTableTimestamp: datetime.datetime | StrictStr | None = None
    NetworkRoutes: list[NetworkManagerNetworkRoute] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
