from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayGetIntegrationRequest(BaseModel):
    restApiId: StrictStr
    resourceId: StrictStr
    httpMethod: StrictStr
