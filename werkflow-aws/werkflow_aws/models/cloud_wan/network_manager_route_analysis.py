from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .network_manager_route_analysis_endpoint_options import NetworkManagerRouteAnalysisEndpointOptions
from .network_manager_route_analysis_path import NetworkManagerRouteAnalysisPath


class NetworkManagerRouteAnalysis(BaseModel):
    GlobalNetworkId: StrictStr | None = None
    OwnerAccountId: StrictStr | None = None
    RouteAnalysisId: StrictStr | None = None
    StartTimestamp: datetime.datetime | StrictStr | None = None
    Status: StrictStr | None = None
    Source: NetworkManagerRouteAnalysisEndpointOptions | None = None
    Destination: NetworkManagerRouteAnalysisEndpointOptions | None = None
    IncludeReturnPath: StrictBool | None = None
    UseMiddleboxes: StrictBool | None = None
    ForwardPath: NetworkManagerRouteAnalysisPath | None = None
    ReturnPath: NetworkManagerRouteAnalysisPath | None = None
