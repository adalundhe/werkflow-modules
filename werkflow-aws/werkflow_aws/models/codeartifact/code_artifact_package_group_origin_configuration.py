from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .code_artifact_package_group_origin_restriction import CodeArtifactPackageGroupOriginRestriction


class CodeArtifactPackageGroupOriginConfiguration(BaseModel):
    restrictions: dict[StrictStr, CodeArtifactPackageGroupOriginRestriction] | None = None
