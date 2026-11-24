from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class APIGatewayPutMethodRequest(BaseModel):
    restApiId: StrictStr
    resourceId: StrictStr
    httpMethod: StrictStr
    authorizationType: StrictStr
    authorizerId: StrictStr | None = None
    apiKeyRequired: StrictBool | None = None
    operationName: StrictStr | None = None
    requestParameters: dict[StrictStr, StrictBool] | None = None
    requestModels: dict[StrictStr, StrictStr] | None = None
    requestValidatorId: StrictStr | None = None
    authorizationScopes: list[StrictStr] | None = None
