from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .api_gateway_api_stage import APIGatewayApiStage
from .api_gateway_quota_settings import APIGatewayQuotaSettings
from .api_gateway_throttle_settings import APIGatewayThrottleSettings


class APIGatewayGetUsagePlanResponse(BaseModel):
    id: StrictStr | None = None
    name: StrictStr | None = None
    description: StrictStr | None = None
    apiStages: list[APIGatewayApiStage] | None = None
    throttle: APIGatewayThrottleSettings | None = None
    quota: APIGatewayQuotaSettings | None = None
    productCode: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
