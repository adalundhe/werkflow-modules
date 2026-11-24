from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .api_gateway_canary_settings import APIGatewayCanarySettings


class APIGatewayCreateStageRequest(BaseModel):
    restApiId: StrictStr
    stageName: StrictStr
    deploymentId: StrictStr
    description: StrictStr | None = None
    cacheClusterEnabled: StrictBool | None = None
    cacheClusterSize: Literal['0.5', '1.6', '6.1', '13.5', '28.4', '58.2', '118', '237'] | None = None
    variables: dict[StrictStr, StrictStr] | None = None
    documentationVersion: StrictStr | None = None
    canarySettings: APIGatewayCanarySettings | None = None
    tracingEnabled: StrictBool | None = None
    tags: dict[StrictStr, StrictStr] | None = None
