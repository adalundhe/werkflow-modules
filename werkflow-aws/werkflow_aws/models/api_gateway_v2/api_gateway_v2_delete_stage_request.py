from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2DeleteStageRequest(BaseModel):
    ApiId: StrictStr
    StageName: StrictStr
