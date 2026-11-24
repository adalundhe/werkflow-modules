from __future__ import annotations
from pydantic import BaseModel
from .code_artifact_repository_description import CodeArtifactRepositoryDescription


class CodeArtifactRepositoryResponse(BaseModel):
    repository: CodeArtifactRepositoryDescription | None = None
