from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .api_gateway_v2_cors import APIGatewayV2Cors


class APIGatewayV2CreateApiRequest(BaseModel):
    Name: StrictStr
    ProtocolType: Literal['WEBSOCKET', 'HTTP']
    ApiKeySelectionExpression: StrictStr | None = None
    CorsConfiguration: APIGatewayV2Cors | None = None
    CredentialsArn: StrictStr | None = None
    Description: StrictStr | None = None
    DisableSchemaValidation: StrictBool | None = None
    DisableExecuteApiEndpoint: StrictBool | None = None
    IpAddressType: Literal['ipv4', 'dualstack'] | None = None
    RouteKey: StrictStr | None = None
    RouteSelectionExpression: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    Target: StrictStr | None = None
    Version: StrictStr | None = None
