from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .api_gateway_v2_parameter_constraints import APIGatewayV2ParameterConstraints


class APIGatewayV2CreateRouteResponseRequest(BaseModel):
    ApiId: StrictStr
    RouteId: StrictStr
    RouteResponseKey: StrictStr
    ModelSelectionExpression: StrictStr | None = None
    ResponseModels: dict[StrictStr, StrictStr] | None = None
    ResponseParameters: dict[StrictStr, APIGatewayV2ParameterConstraints] | None = None
