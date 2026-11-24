from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeArtifactDeletePackageGroupRequest(BaseModel):
    domain: StrictStr
    packageGroup: StrictStr
    domainOwner: StrictStr | None = None
