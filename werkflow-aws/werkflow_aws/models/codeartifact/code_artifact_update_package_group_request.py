from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeArtifactUpdatePackageGroupRequest(BaseModel):
    domain: StrictStr
    packageGroup: StrictStr
    domainOwner: StrictStr | None = None
    contactInfo: StrictStr | None = None
    description: StrictStr | None = None
