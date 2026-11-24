from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .api_gateway_jwt_additional_claim import APIGatewayJwtAdditionalClaim


class APIGatewayJwtIssuerInput(BaseModel):
    issuer: StrictStr
    audiences: list[StrictStr]
    additionalClaims: list[APIGatewayJwtAdditionalClaim] | None = None
