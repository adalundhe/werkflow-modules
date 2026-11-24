from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CodeBuildListBuildsForProjectRequest(BaseModel):
    projectName: StrictStr
    sortOrder: Literal['ASCENDING', 'DESCENDING'] | None = None
    nextToken: StrictStr | None = None
