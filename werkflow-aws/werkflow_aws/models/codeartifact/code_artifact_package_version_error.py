from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeArtifactPackageVersionError(BaseModel):
    errorCode: StrictStr | None = None
    errorMessage: StrictStr | None = None
