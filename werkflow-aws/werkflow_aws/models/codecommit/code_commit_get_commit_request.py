from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCommitGetCommitRequest(BaseModel):
    repositoryName: StrictStr
    commitId: StrictStr
