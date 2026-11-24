from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessUntagResourceRequest(BaseModel):
    resourceARN: StrictStr
    tagKeys: list[StrictStr]
