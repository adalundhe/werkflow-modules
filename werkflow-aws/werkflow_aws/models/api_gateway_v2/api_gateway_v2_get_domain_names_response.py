from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .api_gateway_v2_domain_name import APIGatewayV2DomainName


class APIGatewayV2GetDomainNamesResponse(BaseModel):
    Items: list[APIGatewayV2DomainName] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
