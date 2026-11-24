from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2GetModelTemplateRequest(BaseModel):
    ApiId: StrictStr
    ModelId: StrictStr
