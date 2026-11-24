from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkSpacesThinClientUntagResourceRequest(BaseModel):
    resourceArn: StrictStr
    tagKeys: list[StrictStr]
