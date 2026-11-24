from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .code_commit_comments_for_pull_request import CodeCommitCommentsForPullRequest


class CodeCommitGetCommentsForPullRequestResponse(BaseModel):
    commentsForPullRequestData: list[CodeCommitCommentsForPullRequest] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
