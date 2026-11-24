from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataSyncUntagResourceRequest(BaseModel):
    ResourceArn: StrictStr
    Keys: list[StrictStr]
