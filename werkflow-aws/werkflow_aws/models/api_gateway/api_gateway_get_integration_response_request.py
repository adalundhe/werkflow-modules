from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayGetIntegrationResponseRequest(BaseModel):
    restApiId: StrictStr
    resourceId: StrictStr
    httpMethod: StrictStr
    statusCode: StrictStr
