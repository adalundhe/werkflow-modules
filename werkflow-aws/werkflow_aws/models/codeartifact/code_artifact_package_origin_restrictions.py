from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeArtifactPackageOriginRestrictions(BaseModel):
    publish: StrictStr | None = None
    upstream: StrictStr | None = None
