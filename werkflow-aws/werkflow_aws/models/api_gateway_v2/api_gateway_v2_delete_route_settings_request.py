from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2DeleteRouteSettingsRequest(BaseModel):
    ApiId: StrictStr
    RouteKey: StrictStr
    StageName: StrictStr
