from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCommitGetRepositoryRequest(BaseModel):
    repositoryName: StrictStr
