from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EFSUntagResourceRequest(BaseModel):
    ResourceId: StrictStr
    TagKeys: list[StrictStr]
