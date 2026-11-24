from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .api_gateway_deployment import APIGatewayDeployment


class APIGatewayGetDeploymentsResponse(BaseModel):
    position: StrictStr | None = None
    items: list[APIGatewayDeployment] | None = None
    ResponseMetadata: dict[str, Any] | None = None
