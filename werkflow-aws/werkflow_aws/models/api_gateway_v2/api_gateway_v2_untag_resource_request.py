from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2UntagResourceRequest(BaseModel):
    ResourceArn: StrictStr
    TagKeys: list[StrictStr]
