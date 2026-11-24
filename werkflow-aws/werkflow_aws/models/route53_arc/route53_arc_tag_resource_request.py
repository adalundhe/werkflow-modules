from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53ARCTagResourceRequest(BaseModel):
    ResourceArn: StrictStr
    Tags: dict[StrictStr, StrictStr]
