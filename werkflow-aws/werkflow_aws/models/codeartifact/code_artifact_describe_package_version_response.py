from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .code_artifact_package_version_description import CodeArtifactPackageVersionDescription


class CodeArtifactDescribePackageVersionResponse(BaseModel):
    packageVersion: CodeArtifactPackageVersionDescription | None = None
    ResponseMetadata: dict[str, Any] | None = None
