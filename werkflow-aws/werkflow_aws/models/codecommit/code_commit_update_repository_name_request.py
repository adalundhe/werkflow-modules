from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCommitUpdateRepositoryNameRequest(BaseModel):
    oldName: StrictStr
    newName: StrictStr
