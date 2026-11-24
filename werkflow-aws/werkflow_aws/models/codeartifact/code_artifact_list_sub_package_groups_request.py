from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CodeArtifactListSubPackageGroupsRequest(BaseModel):
    domain: StrictStr
    packageGroup: StrictStr
    domainOwner: StrictStr | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
