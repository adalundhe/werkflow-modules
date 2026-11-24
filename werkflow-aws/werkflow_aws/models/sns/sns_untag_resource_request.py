from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SNSUntagResourceRequest(BaseModel):
    ResourceArn: StrictStr
    TagKeys: list[StrictStr]
