from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayDeleteMethodResponseRequest(BaseModel):
    restApiId: StrictStr
    resourceId: StrictStr
    httpMethod: StrictStr
    statusCode: StrictStr
