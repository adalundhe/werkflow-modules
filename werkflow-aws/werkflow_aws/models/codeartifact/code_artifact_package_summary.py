from __future__ import annotations
from pydantic import BaseModel, StrictStr
from typing import Any


class CodeArtifactPackageSummary(BaseModel):
    format: StrictStr | None = None
    namespace: StrictStr | None = None
    package: StrictStr | None = None
    originConfiguration: dict[str, Any] | None = None
