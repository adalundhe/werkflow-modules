from __future__ import annotations
from pydantic import BaseModel
from .network_manager_path_component import NetworkManagerPathComponent
from .network_manager_route_analysis_completion import NetworkManagerRouteAnalysisCompletion


class NetworkManagerRouteAnalysisPath(BaseModel):
    CompletionStatus: NetworkManagerRouteAnalysisCompletion | None = None
    Path: list[NetworkManagerPathComponent] | None = None
