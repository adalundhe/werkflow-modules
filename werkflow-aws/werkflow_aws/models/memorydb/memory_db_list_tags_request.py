from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MemoryDBListTagsRequest(BaseModel):
    ResourceArn: StrictStr
