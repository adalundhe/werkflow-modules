from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .code_commit_comment import CodeCommitComment
from .code_commit_location import CodeCommitLocation


class CodeCommitCommentsForPullRequest(BaseModel):
    pullRequestId: StrictStr | None = None
    repositoryName: StrictStr | None = None
    beforeCommitId: StrictStr | None = None
    afterCommitId: StrictStr | None = None
    beforeBlobId: StrictStr | None = None
    afterBlobId: StrictStr | None = None
    location: CodeCommitLocation | None = None
    comments: list[CodeCommitComment] | None = None
