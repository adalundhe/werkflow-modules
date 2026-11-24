from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2GetRouteRequest(BaseModel):
    ApiId: StrictStr
    RouteId: StrictStr
