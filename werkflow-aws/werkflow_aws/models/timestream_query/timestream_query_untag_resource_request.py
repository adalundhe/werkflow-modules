from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TimestreamQueryUntagResourceRequest(BaseModel):
    ResourceARN: StrictStr
    TagKeys: list[StrictStr]
