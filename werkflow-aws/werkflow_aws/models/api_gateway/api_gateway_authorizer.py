from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .api_gateway_jwt_configuration import APIGatewayJwtConfiguration


class APIGatewayAuthorizer(BaseModel):
    id: StrictStr | None = None
    name: StrictStr | None = None
    type: StrictStr | None = None
    providerARNs: list[StrictStr] | None = None
    authType: StrictStr | None = None
    authorizerUri: StrictStr | None = None
    authorizerCredentials: StrictStr | None = None
    identitySource: StrictStr | None = None
    identityValidationExpression: StrictStr | None = None
    authorizerResultTtlInSeconds: StrictInt | None = None
    jwtConfiguration: APIGatewayJwtConfiguration | None = None
