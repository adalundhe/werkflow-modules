from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCommitUpdateDefaultBranchRequest(BaseModel):
    repositoryName: StrictStr
    defaultBranchName: StrictStr
