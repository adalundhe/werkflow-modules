from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCommitMergeBranchesByFastForwardRequest(BaseModel):
    repositoryName: StrictStr
    sourceCommitSpecifier: StrictStr
    destinationCommitSpecifier: StrictStr
    targetBranch: StrictStr | None = None
