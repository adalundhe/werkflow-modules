from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class APIGatewayThrottleSettings(BaseModel):
    burstLimit: StrictInt | None = None
    rateLimit: StrictFloat | StrictInt | None = None
