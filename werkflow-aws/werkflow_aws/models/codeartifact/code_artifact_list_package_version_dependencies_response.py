from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .code_artifact_package_dependency import CodeArtifactPackageDependency


class CodeArtifactListPackageVersionDependenciesResponse(BaseModel):
    format: StrictStr | None = None
    namespace: StrictStr | None = None
    package: StrictStr | None = None
    version: StrictStr | None = None
    versionRevision: StrictStr | None = None
    nextToken: StrictStr | None = None
    dependencies: list[CodeArtifactPackageDependency] | None = None
    ResponseMetadata: dict[str, Any] | None = None
