from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .api_gateway_jwt_additional_claim import APIGatewayJwtAdditionalClaim


class APIGatewayJwtIssuer(BaseModel):
    issuer: StrictStr | None = None
    audiences: list[StrictStr] | None = None
    additionalClaims: list[APIGatewayJwtAdditionalClaim] | None = None
    jwksUri: StrictStr | None = None
