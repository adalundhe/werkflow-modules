from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CodeArtifactListRepositoriesInDomainRequest(BaseModel):
    domain: StrictStr
    domainOwner: StrictStr | None = None
    administratorAccount: StrictStr | None = None
    repositoryPrefix: StrictStr | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
