from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TimestreamWriteUntagResourceRequest(BaseModel):
    ResourceARN: StrictStr
    TagKeys: list[StrictStr]
