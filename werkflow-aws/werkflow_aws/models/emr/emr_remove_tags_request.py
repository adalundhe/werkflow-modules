from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EMRRemoveTagsRequest(BaseModel):
    ResourceId: StrictStr
    TagKeys: list[StrictStr]
    ClusterId: StrictStr | None = None
