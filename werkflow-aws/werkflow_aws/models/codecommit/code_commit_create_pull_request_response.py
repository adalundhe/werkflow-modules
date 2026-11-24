from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .code_commit_pull_request import CodeCommitPullRequest


class CodeCommitCreatePullRequestResponse(BaseModel):
    pullRequest: CodeCommitPullRequest | None = None
    ResponseMetadata: dict[str, Any] | None = None
