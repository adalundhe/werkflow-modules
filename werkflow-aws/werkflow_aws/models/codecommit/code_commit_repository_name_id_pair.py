from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCommitRepositoryNameIdPair(BaseModel):
    repositoryName: StrictStr | None = None
    repositoryId: StrictStr | None = None
