from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .code_commit_location import CodeCommitLocation


class CodeCommitPostCommentForComparedCommitRequest(BaseModel):
    repositoryName: StrictStr
    afterCommitId: StrictStr
    content: StrictStr
    beforeCommitId: StrictStr | None = None
    location: CodeCommitLocation | None = None
    clientRequestToken: StrictStr | None = None
