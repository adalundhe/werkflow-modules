from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KendraUntagResourceRequest(BaseModel):
    ResourceARN: StrictStr
    TagKeys: list[StrictStr]
