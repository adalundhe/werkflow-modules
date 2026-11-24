from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class CodeBuildListSandboxesForProjectRequest(BaseModel):
    projectName: StrictStr
    maxResults: StrictInt | None = None
    sortOrder: Literal['ASCENDING', 'DESCENDING'] | None = None
    nextToken: StrictStr | None = None
