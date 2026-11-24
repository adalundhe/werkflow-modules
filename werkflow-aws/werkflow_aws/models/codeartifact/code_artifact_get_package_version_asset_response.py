from __future__ import annotations
from typing import Any
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr


class CodeArtifactGetPackageVersionAssetResponse(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    asset: StrictBytes | Any | None = None
    assetName: StrictStr | None = None
    packageVersion: StrictStr | None = None
    packageVersionRevision: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
