from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CodeCommitListFileCommitHistoryRequest(BaseModel):
    repositoryName: StrictStr
    filePath: StrictStr
    commitSpecifier: StrictStr | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
