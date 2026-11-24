from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .network_manager_core_network_edge import NetworkManagerCoreNetworkEdge
from .network_manager_core_network_network_function_group import NetworkManagerCoreNetworkNetworkFunctionGroup
from .network_manager_core_network_segment import NetworkManagerCoreNetworkSegment
from .network_manager_tag import NetworkManagerTag


class NetworkManagerCoreNetwork(BaseModel):
    GlobalNetworkId: StrictStr | None = None
    CoreNetworkId: StrictStr | None = None
    CoreNetworkArn: StrictStr | None = None
    Description: StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    State: StrictStr | None = None
    Segments: list[NetworkManagerCoreNetworkSegment] | None = None
    NetworkFunctionGroups: list[NetworkManagerCoreNetworkNetworkFunctionGroup] | None = None
    Edges: list[NetworkManagerCoreNetworkEdge] | None = None
    Tags: list[NetworkManagerTag] | None = None
