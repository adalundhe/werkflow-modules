from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .code_commit_location import CodeCommitLocation


class CodeCommitPostCommentForPullRequestRequest(BaseModel):
    pullRequestId: StrictStr
    repositoryName: StrictStr
    beforeCommitId: StrictStr
    afterCommitId: StrictStr
    content: StrictStr
    location: CodeCommitLocation | None = None
    clientRequestToken: StrictStr | None = None
