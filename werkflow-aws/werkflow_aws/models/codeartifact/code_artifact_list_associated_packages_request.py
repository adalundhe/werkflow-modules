from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class CodeArtifactListAssociatedPackagesRequest(BaseModel):
    domain: StrictStr
    packageGroup: StrictStr
    domainOwner: StrictStr | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
    preview: StrictBool | None = None
