from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2ResetAuthorizersCacheRequest(BaseModel):
    ApiId: StrictStr
    StageName: StrictStr
