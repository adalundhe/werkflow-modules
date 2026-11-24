from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayGetStageRequest(BaseModel):
    restApiId: StrictStr
    stageName: StrictStr
