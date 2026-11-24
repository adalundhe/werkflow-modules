from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class CodeArtifactGetPackageVersionReadmeResponse(BaseModel):
    format: StrictStr | None = None
    namespace: StrictStr | None = None
    package: StrictStr | None = None
    version: StrictStr | None = None
    versionRevision: StrictStr | None = None
    readme: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
