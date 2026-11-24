from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .code_artifact_package_origin_configuration import CodeArtifactPackageOriginConfiguration


class CodeArtifactPackageDescription(BaseModel):
    format: StrictStr | None = None
    namespace: StrictStr | None = None
    name: StrictStr | None = None
    originConfiguration: CodeArtifactPackageOriginConfiguration | None = None
