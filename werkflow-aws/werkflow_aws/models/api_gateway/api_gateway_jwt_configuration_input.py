from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .api_gateway_jwt_issuer_input import APIGatewayJwtIssuerInput


class APIGatewayJwtConfigurationInput(BaseModel):
    issuers: list[APIGatewayJwtIssuerInput]
    defaultAlgorithms: list[Literal['RS256', 'RS384', 'RS512', 'ES256', 'ES384', 'ES512']]
