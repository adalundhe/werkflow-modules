from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisVideoUntagResourceRequest(BaseModel):
    ResourceARN: StrictStr
    TagKeyList: list[StrictStr]
