from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class CodeBuildListSharedReportGroupsRequest(BaseModel):
    sortOrder: Literal['ASCENDING', 'DESCENDING'] | None = None
    sortBy: Literal['ARN', 'MODIFIED_TIME'] | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
