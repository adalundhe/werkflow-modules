from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .code_commit_repository_metadata import CodeCommitRepositoryMetadata


class CodeCommitGetRepositoryResponse(BaseModel):
    repositoryMetadata: CodeCommitRepositoryMetadata | None = None
    ResponseMetadata: dict[str, Any] | None = None
