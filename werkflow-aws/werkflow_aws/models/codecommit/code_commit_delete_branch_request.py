from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCommitDeleteBranchRequest(BaseModel):
    repositoryName: StrictStr
    branchName: StrictStr
