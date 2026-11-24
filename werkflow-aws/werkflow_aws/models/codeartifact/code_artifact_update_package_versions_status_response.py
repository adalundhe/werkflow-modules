from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .code_artifact_package_version_error import CodeArtifactPackageVersionError
from .code_artifact_successful_package_version_info import CodeArtifactSuccessfulPackageVersionInfo


class CodeArtifactUpdatePackageVersionsStatusResponse(BaseModel):
    successfulVersions: dict[StrictStr, CodeArtifactSuccessfulPackageVersionInfo] | None = None
    failedVersions: dict[StrictStr, CodeArtifactPackageVersionError] | None = None
    ResponseMetadata: dict[str, Any] | None = None
