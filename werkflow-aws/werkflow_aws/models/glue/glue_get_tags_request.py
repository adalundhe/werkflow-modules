from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueGetTagsRequest(BaseModel):
    ResourceArn: StrictStr
