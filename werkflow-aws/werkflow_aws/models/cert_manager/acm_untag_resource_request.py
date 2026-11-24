from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ACMUntagResourceRequest(BaseModel):
    ResourceArn: StrictStr
    TagKeys: list[StrictStr]
