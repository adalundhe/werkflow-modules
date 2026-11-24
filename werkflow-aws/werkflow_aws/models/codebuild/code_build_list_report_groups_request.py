from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class CodeBuildListReportGroupsRequest(BaseModel):
    sortOrder: Literal['ASCENDING', 'DESCENDING'] | None = None
    sortBy: Literal['NAME', 'CREATED_TIME', 'LAST_MODIFIED_TIME'] | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
