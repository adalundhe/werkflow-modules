from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .api_gateway_api_stage import APIGatewayApiStage
from .api_gateway_quota_settings import APIGatewayQuotaSettings
from .api_gateway_throttle_settings import APIGatewayThrottleSettings


class APIGatewayCreateUsagePlanRequest(BaseModel):
    name: StrictStr
    description: StrictStr | None = None
    apiStages: list[APIGatewayApiStage] | None = None
    throttle: APIGatewayThrottleSettings | None = None
    quota: APIGatewayQuotaSettings | None = None
    tags: dict[StrictStr, StrictStr] | None = None
