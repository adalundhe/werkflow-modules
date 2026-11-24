from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2TagResourceRequest(BaseModel):
    ResourceArn: StrictStr
    Tags: dict[StrictStr, StrictStr] | None = None
