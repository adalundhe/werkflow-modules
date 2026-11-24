from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .api_gateway_domain_name import APIGatewayDomainName


class APIGatewayGetDomainNamesResponse(BaseModel):
    position: StrictStr | None = None
    items: list[APIGatewayDomainName] | None = None
    ResponseMetadata: dict[str, Any] | None = None
