from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .code_artifact_package_description import CodeArtifactPackageDescription


class CodeArtifactDescribePackageResponse(BaseModel):
    package: CodeArtifactPackageDescription | None = None
    ResponseMetadata: dict[str, Any] | None = None
