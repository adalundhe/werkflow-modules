from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MacieUntagResourceRequest(BaseModel):
    resourceArn: StrictStr
    tagKeys: list[StrictStr]
