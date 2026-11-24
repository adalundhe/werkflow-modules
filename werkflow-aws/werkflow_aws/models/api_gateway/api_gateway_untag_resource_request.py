from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayUntagResourceRequest(BaseModel):
    resourceArn: StrictStr
    tagKeys: list[StrictStr]
