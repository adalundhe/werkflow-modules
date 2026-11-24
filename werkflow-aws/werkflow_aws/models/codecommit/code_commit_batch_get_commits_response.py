from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .code_commit_batch_get_commits_error import CodeCommitBatchGetCommitsError
from .code_commit_commit import CodeCommitCommit


class CodeCommitBatchGetCommitsResponse(BaseModel):
    commits: list[CodeCommitCommit] | None = None
    errors: list[CodeCommitBatchGetCommitsError] | None = None
    ResponseMetadata: dict[str, Any] | None = None
