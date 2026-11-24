from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .code_artifact_associated_package import CodeArtifactAssociatedPackage


class CodeArtifactListAssociatedPackagesResponse(BaseModel):
    packages: list[CodeArtifactAssociatedPackage] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
