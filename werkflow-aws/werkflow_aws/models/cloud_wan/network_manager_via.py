from __future__ import annotations
from pydantic import BaseModel
from .network_manager_edge_override import NetworkManagerEdgeOverride
from .network_manager_network_function_group import NetworkManagerNetworkFunctionGroup


class NetworkManagerVia(BaseModel):
    NetworkFunctionGroups: list[NetworkManagerNetworkFunctionGroup] | None = None
    WithEdgeOverrides: list[NetworkManagerEdgeOverride] | None = None
