from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ComprehendUntagResourceRequest(BaseModel):
    ResourceArn: StrictStr
    TagKeys: list[StrictStr]
