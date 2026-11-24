from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCommitBatchGetCommitsRequest(BaseModel):
    commitIds: list[StrictStr]
    repositoryName: StrictStr
