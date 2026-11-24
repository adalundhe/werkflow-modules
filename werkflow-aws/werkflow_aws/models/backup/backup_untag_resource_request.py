from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BackupUntagResourceRequest(BaseModel):
    ResourceArn: StrictStr
    TagKeyList: list[StrictStr]
