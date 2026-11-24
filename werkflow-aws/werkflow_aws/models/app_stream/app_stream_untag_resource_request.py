from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppStreamUntagResourceRequest(BaseModel):
    ResourceArn: StrictStr
    TagKeys: list[StrictStr]
