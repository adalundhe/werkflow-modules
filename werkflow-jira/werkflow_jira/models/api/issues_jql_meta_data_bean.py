from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class IssuesJqlMetaDataBean(BaseModel):
    count: StrictInt | None = None
    maxResults: StrictInt | None = None
    startAt: StrictInt | None = None
    totalCount: StrictInt | None = None
    validationWarnings: list[StrictStr] | None = None
