from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .code_artifact_package_summary import CodeArtifactPackageSummary


class CodeArtifactListPackagesResponse(BaseModel):
    packages: list[CodeArtifactPackageSummary] | None = None
    nextToken: StrictStr | None = None
