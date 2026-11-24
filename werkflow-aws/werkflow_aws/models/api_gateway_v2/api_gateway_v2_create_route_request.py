from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .api_gateway_v2_parameter_constraints import APIGatewayV2ParameterConstraints


class APIGatewayV2CreateRouteRequest(BaseModel):
    ApiId: StrictStr
    RouteKey: StrictStr
    ApiKeyRequired: StrictBool | None = None
    AuthorizationScopes: list[StrictStr] | None = None
    AuthorizationType: Literal['NONE', 'AWS_IAM', 'CUSTOM', 'JWT'] | None = None
    AuthorizerId: StrictStr | None = None
    ModelSelectionExpression: StrictStr | None = None
    OperationName: StrictStr | None = None
    RequestModels: dict[StrictStr, StrictStr] | None = None
    RequestParameters: dict[StrictStr, APIGatewayV2ParameterConstraints] | None = None
    RouteResponseSelectionExpression: StrictStr | None = None
    Target: StrictStr | None = None
