from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .code_commit_comment import CodeCommitComment
from .code_commit_location import CodeCommitLocation


class CodeCommitPostCommentForComparedCommitResponse(BaseModel):
    repositoryName: StrictStr | None = None
    beforeCommitId: StrictStr | None = None
    afterCommitId: StrictStr | None = None
    beforeBlobId: StrictStr | None = None
    afterBlobId: StrictStr | None = None
    location: CodeCommitLocation | None = None
    comment: CodeCommitComment | None = None
    ResponseMetadata: dict[str, Any] | None = None
