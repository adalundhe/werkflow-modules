from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .api_gateway_integration import APIGatewayIntegration
from .api_gateway_method_response import APIGatewayMethodResponse


class APIGatewayPutMethodResponse(BaseModel):
    httpMethod: StrictStr | None = None
    authorizationType: StrictStr | None = None
    authorizerId: StrictStr | None = None
    apiKeyRequired: StrictBool | None = None
    requestValidatorId: StrictStr | None = None
    operationName: StrictStr | None = None
    requestParameters: dict[StrictStr, StrictBool] | None = None
    requestModels: dict[StrictStr, StrictStr] | None = None
    methodResponses: dict[StrictStr, APIGatewayMethodResponse] | None = None
    methodIntegration: APIGatewayIntegration | None = None
    authorizationScopes: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
