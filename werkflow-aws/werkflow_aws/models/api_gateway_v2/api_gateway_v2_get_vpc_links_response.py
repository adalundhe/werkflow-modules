from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .api_gateway_v2_vpc_link import APIGatewayV2VpcLink


class APIGatewayV2GetVpcLinksResponse(BaseModel):
    Items: list[APIGatewayV2VpcLink] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
