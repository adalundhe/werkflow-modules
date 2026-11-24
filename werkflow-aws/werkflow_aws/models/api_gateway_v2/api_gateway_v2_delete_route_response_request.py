from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2DeleteRouteResponseRequest(BaseModel):
    ApiId: StrictStr
    RouteId: StrictStr
    RouteResponseId: StrictStr
