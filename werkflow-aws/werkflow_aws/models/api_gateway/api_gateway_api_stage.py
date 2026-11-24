from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .api_gateway_throttle_settings import APIGatewayThrottleSettings


class APIGatewayApiStage(BaseModel):
    apiId: StrictStr | None = None
    stage: StrictStr | None = None
    throttle: dict[StrictStr, APIGatewayThrottleSettings] | None = None
