from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .network_manager_core_network_network_function_group_identifier import NetworkManagerCoreNetworkNetworkFunctionGroupIdentifier
from .network_manager_core_network_segment_edge_identifier import NetworkManagerCoreNetworkSegmentEdgeIdentifier


class NetworkManagerRouteTableIdentifier(BaseModel):
    TransitGatewayRouteTableArn: StrictStr | None = None
    CoreNetworkSegmentEdge: NetworkManagerCoreNetworkSegmentEdgeIdentifier | None = None
    CoreNetworkNetworkFunctionGroup: NetworkManagerCoreNetworkNetworkFunctionGroupIdentifier | None = None
