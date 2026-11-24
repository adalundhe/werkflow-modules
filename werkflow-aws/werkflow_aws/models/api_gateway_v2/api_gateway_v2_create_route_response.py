from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .api_gateway_v2_parameter_constraints import APIGatewayV2ParameterConstraints


class APIGatewayV2CreateRouteResponse(BaseModel):
    ApiGatewayManaged: StrictBool | None = None
    ApiKeyRequired: StrictBool | None = None
    AuthorizationScopes: list[StrictStr] | None = None
    AuthorizationType: StrictStr | None = None
    AuthorizerId: StrictStr | None = None
    ModelSelectionExpression: StrictStr | None = None
    OperationName: StrictStr | None = None
    RequestModels: dict[StrictStr, StrictStr] | None = None
    RequestParameters: dict[StrictStr, APIGatewayV2ParameterConstraints] | None = None
    RouteId: StrictStr | None = None
    RouteKey: StrictStr | None = None
    RouteResponseSelectionExpression: StrictStr | None = None
    Target: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
