from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53ARCUntagResourceRequest(BaseModel):
    ResourceArn: StrictStr
    TagKeys: list[StrictStr]
