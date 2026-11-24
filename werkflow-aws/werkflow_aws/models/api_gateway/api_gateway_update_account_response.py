from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .api_gateway_throttle_settings import APIGatewayThrottleSettings


class APIGatewayUpdateAccountResponse(BaseModel):
    cloudwatchRoleArn: StrictStr | None = None
    throttleSettings: APIGatewayThrottleSettings | None = None
    features: list[StrictStr] | None = None
    apiKeyVersion: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
