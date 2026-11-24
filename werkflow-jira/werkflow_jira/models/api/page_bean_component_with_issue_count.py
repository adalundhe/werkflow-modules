from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .component_with_issue_count import ComponentWithIssueCount


class PageBeanComponentWithIssueCount(BaseModel):
    isLast: StrictBool | None = None
    maxResults: StrictInt | None = None
    nextPage: StrictStr | None = None
    self: StrictStr | None = None
    startAt: StrictInt | None = None
    total: StrictInt | None = None
    values: list[ComponentWithIssueCount] | None = None
