from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueTagResourceRequest(BaseModel):
    ResourceArn: StrictStr
    TagsToAdd: dict[StrictStr, StrictStr]
