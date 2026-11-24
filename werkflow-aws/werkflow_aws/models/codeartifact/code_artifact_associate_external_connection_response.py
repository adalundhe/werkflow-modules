from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .code_artifact_repository_description_model import CodeArtifactRepositoryDescriptionModel


class CodeArtifactAssociateExternalConnectionResponse(BaseModel):
    repository: CodeArtifactRepositoryDescriptionModel | None = None
    ResponseMetadata: dict[str, Any] | None = None
