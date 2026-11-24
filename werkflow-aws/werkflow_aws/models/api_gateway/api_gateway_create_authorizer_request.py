from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .api_gateway_jwt_configuration_input import APIGatewayJwtConfigurationInput


class APIGatewayCreateAuthorizerRequest(BaseModel):
    restApiId: StrictStr
    name: StrictStr
    type: Literal['TOKEN', 'REQUEST', 'COGNITO_USER_POOLS', 'JWT']
    providerARNs: list[StrictStr] | None = None
    authType: StrictStr | None = None
    authorizerUri: StrictStr | None = None
    authorizerCredentials: StrictStr | None = None
    identitySource: StrictStr | None = None
    identityValidationExpression: StrictStr | None = None
    authorizerResultTtlInSeconds: StrictInt | None = None
    jwtConfiguration: APIGatewayJwtConfigurationInput | None = None
