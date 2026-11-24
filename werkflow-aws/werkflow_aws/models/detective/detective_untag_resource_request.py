from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DetectiveUntagResourceRequest(BaseModel):
    ResourceArn: StrictStr
    TagKeys: list[StrictStr]
