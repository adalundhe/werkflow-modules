from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .code_artifact_asset_summary import CodeArtifactAssetSummary


class CodeArtifactPublishPackageVersionResponse(BaseModel):
    format: StrictStr | None = None
    namespace: StrictStr | None = None
    package: StrictStr | None = None
    version: StrictStr | None = None
    versionRevision: StrictStr | None = None
    status: StrictStr | None = None
    asset: CodeArtifactAssetSummary | None = None
    ResponseMetadata: dict[str, Any] | None = None
