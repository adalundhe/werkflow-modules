from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCommitListTagsForResourceRequest(BaseModel):
    resourceArn: StrictStr
    nextToken: StrictStr | None = None
