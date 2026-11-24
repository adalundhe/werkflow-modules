from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESUntagResourceRequest(BaseModel):
    ResourceArn: StrictStr
    TagKeys: list[StrictStr]
