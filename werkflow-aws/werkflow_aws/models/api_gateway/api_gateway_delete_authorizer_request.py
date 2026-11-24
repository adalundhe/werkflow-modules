from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayDeleteAuthorizerRequest(BaseModel):
    restApiId: StrictStr
    authorizerId: StrictStr
