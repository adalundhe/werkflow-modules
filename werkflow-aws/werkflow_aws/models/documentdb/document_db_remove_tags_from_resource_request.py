from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DocumentDBRemoveTagsFromResourceRequest(BaseModel):
    ResourceName: StrictStr
    TagKeys: list[StrictStr]
