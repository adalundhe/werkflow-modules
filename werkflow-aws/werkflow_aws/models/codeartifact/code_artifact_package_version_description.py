from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .code_artifact_license_info import CodeArtifactLicenseInfo
from .code_artifact_package_version_origin import CodeArtifactPackageVersionOrigin


class CodeArtifactPackageVersionDescription(BaseModel):
    format: StrictStr | None = None
    namespace: StrictStr | None = None
    packageName: StrictStr | None = None
    displayName: StrictStr | None = None
    version: StrictStr | None = None
    summary: StrictStr | None = None
    homePage: StrictStr | None = None
    sourceCodeRepository: StrictStr | None = None
    publishedTime: datetime.datetime | StrictStr | None = None
    licenses: list[CodeArtifactLicenseInfo] | None = None
    revision: StrictStr | None = None
    status: StrictStr | None = None
    origin: CodeArtifactPackageVersionOrigin | None = None
