from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .network_manager_route_analysis_endpoint_options_specification import NetworkManagerRouteAnalysisEndpointOptionsSpecification


class NetworkManagerStartRouteAnalysisRequest(BaseModel):
    GlobalNetworkId: StrictStr
    Source: NetworkManagerRouteAnalysisEndpointOptionsSpecification
    Destination: NetworkManagerRouteAnalysisEndpointOptionsSpecification
    IncludeReturnPath: StrictBool | None = None
    UseMiddleboxes: StrictBool | None = None
