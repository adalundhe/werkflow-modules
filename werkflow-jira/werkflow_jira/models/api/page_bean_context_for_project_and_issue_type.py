from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .context_for_project_and_issue_type import ContextForProjectAndIssueType


class PageBeanContextForProjectAndIssueType(BaseModel):
    isLast: StrictBool | None = None
    maxResults: StrictInt | None = None
    nextPage: StrictStr | None = None
    self: StrictStr | None = None
    startAt: StrictInt | None = None
    total: StrictInt | None = None
    values: list[ContextForProjectAndIssueType] | None = None
