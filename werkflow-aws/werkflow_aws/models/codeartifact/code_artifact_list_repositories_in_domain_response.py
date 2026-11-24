from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .code_artifact_repository_summary_model import CodeArtifactRepositorySummaryModel


class CodeArtifactListRepositoriesInDomainResponse(BaseModel):
    repositories: list[CodeArtifactRepositorySummaryModel] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
