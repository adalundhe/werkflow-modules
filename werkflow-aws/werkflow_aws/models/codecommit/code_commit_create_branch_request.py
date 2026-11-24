from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCommitCreateBranchRequest(BaseModel):
    repositoryName: StrictStr
    branchName: StrictStr
    commitId: StrictStr
