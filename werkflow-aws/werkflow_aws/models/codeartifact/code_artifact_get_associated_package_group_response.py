from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .code_artifact_package_group_description import CodeArtifactPackageGroupDescription


class CodeArtifactGetAssociatedPackageGroupResponse(BaseModel):
    packageGroup: CodeArtifactPackageGroupDescription | None = None
    associationType: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
