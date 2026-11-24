from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCommitBatchGetRepositoriesRequest(BaseModel):
    repositoryNames: list[StrictStr]
