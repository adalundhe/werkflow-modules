from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .api_gateway_jwt_issuer import APIGatewayJwtIssuer


class APIGatewayJwtConfiguration(BaseModel):
    issuers: list[APIGatewayJwtIssuer] | None = None
    defaultAlgorithms: list[StrictStr] | None = None
