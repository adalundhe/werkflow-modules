from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FISUntagResourceRequest(BaseModel):
    resourceArn: StrictStr
    tagKeys: list[StrictStr] | None = None
