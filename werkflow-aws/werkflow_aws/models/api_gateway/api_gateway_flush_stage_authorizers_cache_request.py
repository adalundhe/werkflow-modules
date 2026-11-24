from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayFlushStageAuthorizersCacheRequest(BaseModel):
    restApiId: StrictStr
    stageName: StrictStr
