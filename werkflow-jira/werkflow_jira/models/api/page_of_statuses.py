from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .jira_status import JiraStatus


class PageOfStatuses(BaseModel):
    isLast: StrictBool | None = None
    maxResults: StrictInt | None = None
    nextPage: StrictStr | None = None
    self: StrictStr | None = None
    startAt: StrictInt | None = None
    total: StrictInt | None = None
    values: list[JiraStatus] | None = None
