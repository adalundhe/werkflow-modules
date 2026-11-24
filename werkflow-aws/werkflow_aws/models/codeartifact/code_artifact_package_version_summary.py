from __future__ import annotations
from pydantic import BaseModel, StrictStr
from typing import Any


class CodeArtifactPackageVersionSummary(BaseModel):
    version: StrictStr | None = None
    revision: StrictStr | None = None
    status: StrictStr | None = None
    origin: dict[str, Any] | None = None
