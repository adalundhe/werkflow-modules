from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .issue_type_screen_schemes_projects import IssueTypeScreenSchemesProjects


class PageBeanIssueTypeScreenSchemesProjects(BaseModel):
    isLast: StrictBool | None = None
    maxResults: StrictInt | None = None
    nextPage: StrictStr | None = None
    self: StrictStr | None = None
    startAt: StrictInt | None = None
    total: StrictInt | None = None
    values: list[IssueTypeScreenSchemesProjects] | None = None
