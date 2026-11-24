from __future__ import annotations
from pydantic import BaseModel
from .api_gateway_v2_identifier_parts import APIGatewayV2IdentifierParts


class APIGatewayV2RestEndpointIdentifier(BaseModel):
    IdentifierParts: APIGatewayV2IdentifierParts | None = None
