from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2GetStageRequest(BaseModel):
    ApiId: StrictStr
    StageName: StrictStr
