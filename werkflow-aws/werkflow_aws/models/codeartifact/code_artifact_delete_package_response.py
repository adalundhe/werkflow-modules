from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .code_artifact_package_summary_model import CodeArtifactPackageSummaryModel


class CodeArtifactDeletePackageResponse(BaseModel):
    deletedPackage: CodeArtifactPackageSummaryModel | None = None
    ResponseMetadata: dict[str, Any] | None = None
