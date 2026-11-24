from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectoryServiceRemoveTagsFromResourceRequest(BaseModel):
    ResourceId: StrictStr
    TagKeys: list[StrictStr]
