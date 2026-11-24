from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayDeleteModelRequest(BaseModel):
    restApiId: StrictStr
    modelName: StrictStr
