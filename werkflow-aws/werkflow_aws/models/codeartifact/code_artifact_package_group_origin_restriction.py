from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .code_artifact_package_group_reference import CodeArtifactPackageGroupReference


class CodeArtifactPackageGroupOriginRestriction(BaseModel):
    mode: StrictStr | None = None
    effectiveMode: StrictStr | None = None
    inheritedFrom: CodeArtifactPackageGroupReference | None = None
    repositoriesCount: StrictInt | None = None
