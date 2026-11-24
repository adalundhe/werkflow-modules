from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CodeCommitGetCommentsForComparedCommitRequest(BaseModel):
    repositoryName: StrictStr
    afterCommitId: StrictStr
    beforeCommitId: StrictStr | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
