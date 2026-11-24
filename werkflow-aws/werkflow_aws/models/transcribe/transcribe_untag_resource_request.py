from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TranscribeUntagResourceRequest(BaseModel):
    ResourceArn: StrictStr
    TagKeys: list[StrictStr]
