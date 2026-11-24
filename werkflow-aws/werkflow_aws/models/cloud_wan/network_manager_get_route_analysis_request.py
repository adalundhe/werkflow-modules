from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerGetRouteAnalysisRequest(BaseModel):
    GlobalNetworkId: StrictStr
    RouteAnalysisId: StrictStr
