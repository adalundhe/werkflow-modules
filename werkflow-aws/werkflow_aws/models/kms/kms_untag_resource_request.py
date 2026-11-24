from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KMSUntagResourceRequest(BaseModel):
    KeyId: StrictStr
    TagKeys: list[StrictStr]
