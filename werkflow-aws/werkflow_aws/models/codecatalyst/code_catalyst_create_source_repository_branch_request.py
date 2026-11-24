from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCatalystCreateSourceRepositoryBranchRequest(BaseModel):
    spaceName: StrictStr
    projectName: StrictStr
    sourceRepositoryName: StrictStr
    name: StrictStr
    headCommitId: StrictStr | None = None
