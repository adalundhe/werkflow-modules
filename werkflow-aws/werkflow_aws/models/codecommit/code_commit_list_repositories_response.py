from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .code_commit_repository_name_id_pair import CodeCommitRepositoryNameIdPair


class CodeCommitListRepositoriesResponse(BaseModel):
    repositories: list[CodeCommitRepositoryNameIdPair] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
