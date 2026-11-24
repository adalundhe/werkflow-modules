from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CodeBuildListProjectsRequest(BaseModel):
    sortBy: Literal['NAME', 'CREATED_TIME', 'LAST_MODIFIED_TIME'] | None = None
    sortOrder: Literal['ASCENDING', 'DESCENDING'] | None = None
    nextToken: StrictStr | None = None
