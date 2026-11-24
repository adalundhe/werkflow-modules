from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CodeCommitGetCommentsForPullRequestRequest(BaseModel):
    pullRequestId: StrictStr
    repositoryName: StrictStr | None = None
    beforeCommitId: StrictStr | None = None
    afterCommitId: StrictStr | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
