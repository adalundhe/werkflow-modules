from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeGuruUntagResourceRequest(BaseModel):
    resourceArn: StrictStr
    TagKeys: list[StrictStr]
