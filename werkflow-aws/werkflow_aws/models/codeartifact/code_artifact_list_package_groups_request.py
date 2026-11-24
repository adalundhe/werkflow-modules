from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CodeArtifactListPackageGroupsRequest(BaseModel):
    domain: StrictStr
    domainOwner: StrictStr | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
    prefix: StrictStr | None = None
