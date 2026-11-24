from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EFSDeleteTagsRequest(BaseModel):
    FileSystemId: StrictStr
    TagKeys: list[StrictStr]
