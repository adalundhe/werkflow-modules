from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCommitListBranchesRequest(BaseModel):
    repositoryName: StrictStr
    nextToken: StrictStr | None = None
