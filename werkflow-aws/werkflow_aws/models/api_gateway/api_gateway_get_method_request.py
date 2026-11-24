from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayGetMethodRequest(BaseModel):
    restApiId: StrictStr
    resourceId: StrictStr
    httpMethod: StrictStr
