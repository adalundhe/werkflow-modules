from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeArtifactSuccessfulPackageVersionInfo(BaseModel):
    revision: StrictStr | None = None
    status: StrictStr | None = None
