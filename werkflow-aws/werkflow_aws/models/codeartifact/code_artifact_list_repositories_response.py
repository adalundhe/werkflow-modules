from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .code_artifact_repository_summary import CodeArtifactRepositorySummary


class CodeArtifactListRepositoriesResponse(BaseModel):
    repositories: list[CodeArtifactRepositorySummary] | None = None
    nextToken: StrictStr | None = None
