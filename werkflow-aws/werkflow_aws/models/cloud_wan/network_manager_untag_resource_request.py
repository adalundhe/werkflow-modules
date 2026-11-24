from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerUntagResourceRequest(BaseModel):
    ResourceArn: StrictStr
    TagKeys: list[StrictStr]
