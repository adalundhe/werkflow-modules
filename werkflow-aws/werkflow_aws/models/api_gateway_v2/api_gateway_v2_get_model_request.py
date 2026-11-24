from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2GetModelRequest(BaseModel):
    ApiId: StrictStr
    ModelId: StrictStr
