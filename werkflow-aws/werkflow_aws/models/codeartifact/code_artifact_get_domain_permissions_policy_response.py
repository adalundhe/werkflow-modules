from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .code_artifact_resource_policy import CodeArtifactResourcePolicy


class CodeArtifactGetDomainPermissionsPolicyResponse(BaseModel):
    policy: CodeArtifactResourcePolicy | None = None
    ResponseMetadata: dict[str, Any] | None = None
