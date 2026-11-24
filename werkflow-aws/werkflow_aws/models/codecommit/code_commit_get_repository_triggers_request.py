from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCommitGetRepositoryTriggersRequest(BaseModel):
    repositoryName: StrictStr
