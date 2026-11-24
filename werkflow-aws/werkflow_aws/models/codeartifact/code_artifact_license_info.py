from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeArtifactLicenseInfo(BaseModel):
    name: StrictStr | None = None
    url: StrictStr | None = None
