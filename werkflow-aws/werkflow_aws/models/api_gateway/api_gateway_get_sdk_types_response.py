from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .api_gateway_sdk_type import APIGatewaySdkType


class APIGatewayGetSdkTypesResponse(BaseModel):
    position: StrictStr | None = None
    items: list[APIGatewaySdkType] | None = None
    ResponseMetadata: dict[str, Any] | None = None
