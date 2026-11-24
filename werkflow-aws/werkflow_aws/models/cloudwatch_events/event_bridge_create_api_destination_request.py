from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class EventBridgeCreateApiDestinationRequest(BaseModel):
    Name: StrictStr
    ConnectionArn: StrictStr
    InvocationEndpoint: StrictStr
    HttpMethod: Literal['POST', 'GET', 'HEAD', 'OPTIONS', 'PUT', 'PATCH', 'DELETE']
    Description: StrictStr | None = None
    InvocationRateLimitPerSecond: StrictInt | None = None
