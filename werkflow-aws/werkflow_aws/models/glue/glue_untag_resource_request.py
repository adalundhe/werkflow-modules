from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueUntagResourceRequest(BaseModel):
    ResourceArn: StrictStr
    TagsToRemove: list[StrictStr]
