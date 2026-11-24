from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2GetRouteResponseRequest(BaseModel):
    ApiId: StrictStr
    RouteId: StrictStr
    RouteResponseId: StrictStr
