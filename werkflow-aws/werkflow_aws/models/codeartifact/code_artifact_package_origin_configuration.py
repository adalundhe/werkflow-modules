from __future__ import annotations
from pydantic import BaseModel
from .code_artifact_package_origin_restrictions import CodeArtifactPackageOriginRestrictions


class CodeArtifactPackageOriginConfiguration(BaseModel):
    restrictions: CodeArtifactPackageOriginRestrictions | None = None
