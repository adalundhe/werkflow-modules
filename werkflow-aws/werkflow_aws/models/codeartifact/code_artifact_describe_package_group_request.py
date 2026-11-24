from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeArtifactDescribePackageGroupRequest(BaseModel):
    domain: StrictStr
    packageGroup: StrictStr
    domainOwner: StrictStr | None = None
