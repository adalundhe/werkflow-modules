from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSRemoveTagsFromResourceRequest(BaseModel):
    ResourceName: StrictStr
    TagKeys: list[StrictStr]
