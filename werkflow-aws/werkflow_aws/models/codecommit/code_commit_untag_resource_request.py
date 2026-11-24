from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCommitUntagResourceRequest(BaseModel):
    resourceArn: StrictStr
    tagKeys: list[StrictStr]
