from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayFlushStageCacheRequest(BaseModel):
    restApiId: StrictStr
    stageName: StrictStr
