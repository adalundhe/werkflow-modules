from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCommitTagResourceRequest(BaseModel):
    resourceArn: StrictStr
    tags: dict[StrictStr, StrictStr]
