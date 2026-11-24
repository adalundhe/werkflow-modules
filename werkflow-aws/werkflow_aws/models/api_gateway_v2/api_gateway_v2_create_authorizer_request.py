from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .api_gateway_v2_jwt_configuration import APIGatewayV2JWTConfiguration


class APIGatewayV2CreateAuthorizerRequest(BaseModel):
    ApiId: StrictStr
    AuthorizerType: Literal['REQUEST', 'JWT']
    IdentitySource: list[StrictStr]
    Name: StrictStr
    AuthorizerCredentialsArn: StrictStr | None = None
    AuthorizerPayloadFormatVersion: StrictStr | None = None
    AuthorizerResultTtlInSeconds: StrictInt | None = None
    AuthorizerUri: StrictStr | None = None
    EnableSimpleResponses: StrictBool | None = None
    IdentityValidationExpression: StrictStr | None = None
    JwtConfiguration: APIGatewayV2JWTConfiguration | None = None
