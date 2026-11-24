from __future__ import annotations
from pydantic import BaseModel, StrictStr
from typing import Any


class CodeArtifactDeletePackageVersionsResponse(BaseModel):
    successfulVersions: dict[StrictStr, dict[str, Any]] | None = None
    failedVersions: dict[StrictStr, dict[str, Any]] | None = None
