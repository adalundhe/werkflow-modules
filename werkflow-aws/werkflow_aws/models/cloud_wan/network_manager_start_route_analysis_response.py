from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .network_manager_route_analysis import NetworkManagerRouteAnalysis


class NetworkManagerStartRouteAnalysisResponse(BaseModel):
    RouteAnalysis: NetworkManagerRouteAnalysis | None = None
    ResponseMetadata: dict[str, Any] | None = None
