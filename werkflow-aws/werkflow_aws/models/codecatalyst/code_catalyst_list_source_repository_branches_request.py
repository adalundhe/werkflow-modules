from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CodeCatalystListSourceRepositoryBranchesRequest(BaseModel):
    spaceName: StrictStr
    projectName: StrictStr
    sourceRepositoryName: StrictStr
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
