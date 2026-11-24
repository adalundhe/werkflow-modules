from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class EventBridgeUpdateApiDestinationRequest(BaseModel):
    Name: StrictStr
    Description: StrictStr | None = None
    ConnectionArn: StrictStr | None = None
    InvocationEndpoint: StrictStr | None = None
    HttpMethod: Literal['POST', 'GET', 'HEAD', 'OPTIONS', 'PUT', 'PATCH', 'DELETE'] | None = None
    InvocationRateLimitPerSecond: StrictInt | None = None
