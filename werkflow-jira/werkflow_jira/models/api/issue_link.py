from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .issue_link_type import IssueLinkType
from .linked_issue import LinkedIssue


class IssueLink(BaseModel):
    id: StrictStr | None = None
    inwardIssue: LinkedIssue | None = None
    outwardIssue: LinkedIssue | None = None
    self: StrictStr | None = None
    type: IssueLinkType | None = None
