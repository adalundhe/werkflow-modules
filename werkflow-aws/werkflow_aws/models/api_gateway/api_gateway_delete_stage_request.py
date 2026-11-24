from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayDeleteStageRequest(BaseModel):
    restApiId: StrictStr
    stageName: StrictStr
