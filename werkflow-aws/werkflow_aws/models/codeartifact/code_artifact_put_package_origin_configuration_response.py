from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .code_artifact_package_origin_configuration import CodeArtifactPackageOriginConfiguration


class CodeArtifactPutPackageOriginConfigurationResponse(BaseModel):
    originConfiguration: CodeArtifactPackageOriginConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
