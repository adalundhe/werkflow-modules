from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .api_gateway_stage_key import APIGatewayStageKey


class APIGatewayCreateApiKeyRequest(BaseModel):
    name: StrictStr | None = None
    description: StrictStr | None = None
    enabled: StrictBool | None = None
    generateDistinctId: StrictBool | None = None
    value: StrictStr | None = None
    stageKeys: list[APIGatewayStageKey] | None = None
    customerId: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
