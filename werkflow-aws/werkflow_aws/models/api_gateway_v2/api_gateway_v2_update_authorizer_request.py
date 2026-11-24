from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .api_gateway_v2_jwt_configuration import APIGatewayV2JWTConfiguration


class APIGatewayV2UpdateAuthorizerRequest(BaseModel):
    ApiId: StrictStr
    AuthorizerId: StrictStr
    AuthorizerCredentialsArn: StrictStr | None = None
    AuthorizerPayloadFormatVersion: StrictStr | None = None
    AuthorizerResultTtlInSeconds: StrictInt | None = None
    AuthorizerType: Literal['REQUEST', 'JWT'] | None = None
    AuthorizerUri: StrictStr | None = None
    EnableSimpleResponses: StrictBool | None = None
    IdentitySource: list[StrictStr] | None = None
    IdentityValidationExpression: StrictStr | None = None
    JwtConfiguration: APIGatewayV2JWTConfiguration | None = None
    Name: StrictStr | None = None
