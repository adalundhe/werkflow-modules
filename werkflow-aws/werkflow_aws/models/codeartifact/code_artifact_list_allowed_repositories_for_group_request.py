from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class CodeArtifactListAllowedRepositoriesForGroupRequest(BaseModel):
    domain: StrictStr
    packageGroup: StrictStr
    originRestrictionType: Literal['EXTERNAL_UPSTREAM', 'INTERNAL_UPSTREAM', 'PUBLISH']
    domainOwner: StrictStr | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
