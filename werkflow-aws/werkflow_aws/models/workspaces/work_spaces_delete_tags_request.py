from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkSpacesDeleteTagsRequest(BaseModel):
    ResourceId: StrictStr
    TagKeys: list[StrictStr]
