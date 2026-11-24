from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2GetRouteResponsesRequest(BaseModel):
    ApiId: StrictStr
    RouteId: StrictStr
    MaxResults: StrictStr | None = None
    NextToken: StrictStr | None = None
