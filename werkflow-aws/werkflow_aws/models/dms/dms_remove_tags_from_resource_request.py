from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DMSRemoveTagsFromResourceRequest(BaseModel):
    ResourceArn: StrictStr
    TagKeys: list[StrictStr]
