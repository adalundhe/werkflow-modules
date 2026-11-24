from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayGetAuthorizerRequest(BaseModel):
    restApiId: StrictStr
    authorizerId: StrictStr
