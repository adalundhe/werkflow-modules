from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class APIGatewayGetModelRequest(BaseModel):
    restApiId: StrictStr
    modelName: StrictStr
    flatten: StrictBool | None = None
