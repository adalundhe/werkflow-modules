from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MWAAUntagResourceRequest(BaseModel):
    ResourceArn: StrictStr
    tagKeys: list[StrictStr]
