from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .api_gateway_v2_jwt_configuration import APIGatewayV2JWTConfiguration


class APIGatewayV2Authorizer(BaseModel):
    AuthorizerCredentialsArn: StrictStr | None = None
    AuthorizerId: StrictStr | None = None
    AuthorizerPayloadFormatVersion: StrictStr | None = None
    AuthorizerResultTtlInSeconds: StrictInt | None = None
    AuthorizerType: StrictStr | None = None
    AuthorizerUri: StrictStr | None = None
    EnableSimpleResponses: StrictBool | None = None
    IdentitySource: list[StrictStr] | None = None
    IdentityValidationExpression: StrictStr | None = None
    JwtConfiguration: APIGatewayV2JWTConfiguration | None = None
    Name: StrictStr | None = None
