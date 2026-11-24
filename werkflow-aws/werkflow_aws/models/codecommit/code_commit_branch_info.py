from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCommitBranchInfo(BaseModel):
    branchName: StrictStr | None = None
    commitId: StrictStr | None = None
