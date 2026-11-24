from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class CodeBuildListSharedProjectsRequest(BaseModel):
    sortBy: Literal['ARN', 'MODIFIED_TIME'] | None = None
    sortOrder: Literal['ASCENDING', 'DESCENDING'] | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
