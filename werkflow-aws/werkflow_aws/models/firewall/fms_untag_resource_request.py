from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FMSUntagResourceRequest(BaseModel):
    ResourceArn: StrictStr
    TagKeys: list[StrictStr]
