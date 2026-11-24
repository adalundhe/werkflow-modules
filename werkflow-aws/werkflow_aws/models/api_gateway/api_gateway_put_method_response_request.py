from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class APIGatewayPutMethodResponseRequest(BaseModel):
    restApiId: StrictStr
    resourceId: StrictStr
    httpMethod: StrictStr
    statusCode: StrictStr
    responseParameters: dict[StrictStr, StrictBool] | None = None
    responseModels: dict[StrictStr, StrictStr] | None = None
