from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NeptuneRemoveTagsFromResourceRequest(BaseModel):
    ResourceName: StrictStr
    TagKeys: list[StrictStr]
