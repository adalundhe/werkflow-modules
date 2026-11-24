from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .code_artifact_package_group_description import CodeArtifactPackageGroupDescription


class CodeArtifactCreatePackageGroupResponse(BaseModel):
    packageGroup: CodeArtifactPackageGroupDescription | None = None
    ResponseMetadata: dict[str, Any] | None = None
