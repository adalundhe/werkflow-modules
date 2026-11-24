from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2GetAuthorizerRequest(BaseModel):
    ApiId: StrictStr
    AuthorizerId: StrictStr
