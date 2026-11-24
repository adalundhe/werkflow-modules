from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppRunnerUntagResourceRequest(BaseModel):
    ResourceArn: StrictStr
    TagKeys: list[StrictStr]
