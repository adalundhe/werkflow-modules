from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2DeleteRouteRequest(BaseModel):
    ApiId: StrictStr
    RouteId: StrictStr
