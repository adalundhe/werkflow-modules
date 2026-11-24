from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class CodeCommitListPullRequestsRequest(BaseModel):
    repositoryName: StrictStr
    authorArn: StrictStr | None = None
    pullRequestStatus: Literal['OPEN', 'CLOSED'] | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
