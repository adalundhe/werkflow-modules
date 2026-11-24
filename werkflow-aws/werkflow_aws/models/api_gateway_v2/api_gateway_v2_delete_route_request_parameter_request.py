from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2DeleteRouteRequestParameterRequest(BaseModel):
    ApiId: StrictStr
    RequestParameterKey: StrictStr
    RouteId: StrictStr
