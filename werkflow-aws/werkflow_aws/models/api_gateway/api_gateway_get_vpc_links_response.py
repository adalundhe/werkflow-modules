from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .api_gateway_vpc_link import APIGatewayVpcLink


class APIGatewayGetVpcLinksResponse(BaseModel):
    position: StrictStr | None = None
    items: list[APIGatewayVpcLink] | None = None
    ResponseMetadata: dict[str, Any] | None = None
