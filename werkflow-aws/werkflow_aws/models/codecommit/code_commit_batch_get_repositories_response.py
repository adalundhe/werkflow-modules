from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .code_commit_batch_get_repositories_error import CodeCommitBatchGetRepositoriesError
from .code_commit_repository_metadata import CodeCommitRepositoryMetadata


class CodeCommitBatchGetRepositoriesResponse(BaseModel):
    repositories: list[CodeCommitRepositoryMetadata] | None = None
    repositoriesNotFound: list[StrictStr] | None = None
    errors: list[CodeCommitBatchGetRepositoriesError] | None = None
    ResponseMetadata: dict[str, Any] | None = None
