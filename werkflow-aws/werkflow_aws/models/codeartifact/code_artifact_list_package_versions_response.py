from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .code_artifact_package_version_summary import CodeArtifactPackageVersionSummary


class CodeArtifactListPackageVersionsResponse(BaseModel):
    defaultDisplayVersion: StrictStr | None = None
    format: StrictStr | None = None
    namespace: StrictStr | None = None
    package: StrictStr | None = None
    versions: list[CodeArtifactPackageVersionSummary] | None = None
    nextToken: StrictStr | None = None
