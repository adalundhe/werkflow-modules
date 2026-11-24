from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCommitGetBranchRequest(BaseModel):
    repositoryName: StrictStr | None = None
    branchName: StrictStr | None = None
